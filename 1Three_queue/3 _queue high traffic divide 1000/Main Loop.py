# Main Loop
import Functions as ht #ht for heavy traffic
import scipy.stats as st
import csv
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import multiprocessing as mp

VLIST = [[1/2, 0, 1/2, 1/2]]
#a list of lists whose elements are the values of v in the order of v11, v22, v12, v21
SLIST = [s/10 for s in range(1,10)] + [s/1000 for s in range(901,1000)]
#SLIST = [s/100 for s in range(91,100)]
# a list iof traffic intensity values from 0.1, 0.2 to 0.9,0.901,..., 0.91,0.911, 0.999
PLIST = ["MaxWt", "Pri_E", "MaxSize_PriMaxWt"]
# a list of selection policies

ITER = 10000000
#time length of simulation

Total_figures = [] #Initialize the list to store data for the 3 figures
# for 3 set of V values

def get_S_qavg_lists(Vs, policy, S):
    qavg = 0
    qlist = [0, 0, 0, 0] # a list for values of the average queue length
    # in the order of q11, q12, q21
    for t in range(1, ITER + 1):
        lambdaRv_list = ht.arrivalRate(Vs[0], Vs[1], Vs[2], Vs[3], S)
        # a list for random variables of the arrival rate, normal distr
        # in the order of lambda11_norm, lambda12_norm, lambda21_norm
        if policy == "MaxWt":
            qlist = ht.MaxWt(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        elif policy == "Pri_E":
            qlist = ht.Pri_E(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        elif policy == "MaxSize_PriMaxWt":
            qlist = ht.MaxSize_PriMaxWt(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        # Update qlist
        if t > ITER*4/10: #Throwing away the first 40%
            tau = t-ITER*4/10
            qavg = ht.updateQavg(qlist, qavg, tau)
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
            with open(str(Vs) + '.csv', 'a', newline = '') as out:
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



