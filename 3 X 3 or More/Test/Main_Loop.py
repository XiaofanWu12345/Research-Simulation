# Main Loop
import Functions as ht #ht for heavy traffic
import scipy.stats as st
import csv
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import multiprocessing as mp

N = 3
#We want an 3 X 3 switch
VLIST = [ht.initializeMatrix(N)[0]]
#Initialize a list of lists whose elements are the values of v and the queue length matrix
SLIST = [s/10 for s in range(1,10)] + [s/100 for s in range(91,96)] + [s/1000 for s in range(960,1000)]
#SLIST = [s/100 for s in range(91,100)]
# a list iof traffic intensity values from 0.1, 0.2 to 0.9,0.91,0.92,...,0.96, 0.961,0.962,...,0.999
PLIST = ["MaxWt"]
# a list of selection policies

ITER = 10000
#time length of simulation

def get_S_qavg_lists(Vs, policy, S):
    qavg = 0
    Queues = ht.initializeMatrix(N)[1]
    lambdaRv_list = ht.arrivalRate(Vs, S)
    #A matrix of lambdas -- arrival rates
    for t in range(1, ITER + 1):
        Queues = ht.updateQ(Queues, lambdaRv_list)
        if policy == "MaxWt":
            Queues = ht.MaxWt(Queues)
        elif policy == "MaxSize_random":
            Queues = ht.MaxSize_random(Queues)
        elif policy == "MaxSize_PriMaxWt":
            Queues = ht.MaxSize_PriMaxWt(Queues)
        elif policy == "MaxSize_PriMaxWtLog":
            Queues = ht.MaxSize_PriMaxWtLog(Queues)
        # Update Queues
        if t > ITER*6/10:
            tau = t-ITER*6/10
            qavg = ht.updateQavg(Queues, qavg, tau)
            # Update the total average queue length
            epsilon_times_qavg = (1 - S) * qavg # epsilon = (1 - S)
    return [S, qavg, epsilon_times_qavg] # Return S and its corresponding average queue length

def main(args):
    for Vs in VLIST:
        for policy in PLIST:
            num_cores = mp.cpu_count()
            S_qavg_lists = Parallel(n_jobs = num_cores)(delayed(get_S_qavg_lists)(Vs, policy, S) for S in SLIST)
            S_qavg_lists = sorted(S_qavg_lists, key = lambda sub: sub[0])
            S_headers = [sublist[0] for sublist in S_qavg_lists]
            # a list of S values in ascending order
            qavg_values = [sublist[1] for sublist in S_qavg_lists]
            # a list of qavg values whose order follows the corresponding S value's
            # order
            etq_values = [sublist[2] for sublist in S_qavg_lists]
            # a list of epsilon times qavg values whose order follows the corresponding S value's
            # order
            with open(str(VLIST.index(Vs)) + 'th Vs' + '.csv', 'a', newline = '') as out:
                csvout = csv.writer(out)
                if PLIST.index(policy) == 0:
                    csvout.writerow([''] + [''] + S_headers)
                csvout.writerow([policy] + ['Avg Queue Length'] + qavg_values)
                csvout.writerow([''] + ['(1 - S) * qavg'] + etq_values)
            # Write the traffic intensity values and their corresponding total
            # average queue length and (1-S)*qavg in different policies, each file for one
            # set of V values

if __name__ == "__main__":
    import sys
    main(sys.argv)



