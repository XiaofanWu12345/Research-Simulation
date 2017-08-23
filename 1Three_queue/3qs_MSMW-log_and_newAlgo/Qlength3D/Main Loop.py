# Main Loop
import Functions as ht #ht for heavy traffic
import scipy.stats as st
import csv
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import multiprocessing as mp
import math

VLIST = [[1/2, 0, 1/2, 1/2]]
#a list of lists whose elements are the values of v in the order of v11, v22, v12, v21
SLIST = [s/10 for s in range(1,10)] + [s/100 for s in range(91,96)] + [s/1000 for s in range(960,1000)]
#SLIST = [s/100 for s in range(91,100)]
# a list iof traffic intensity values from 0.1, 0.2 to 0.9,0.91,0.92,...,0.96, 0.961,0.962,...,0.999
PLIST = ["MaxWt", "Pri_E", "MaxSize_PriMaxWt","MaxSize_PriMaxWtLog", "Algo_2", "Algo_3"]
# a list of selection policies

ITER = 1000000
#time length of simulation

def get_Plot_lists(Vs, policy, S):
    plotlistx = []
    plotlisty = []
    plotlistz = []
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
        elif policy == "MaxSize_PriMaxWtLog":
            qlist = ht.MaxSize_PriMaxWtLog(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        elif policy == "Algo_2":
            qlist = ht.Algo_2(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        elif policy == "Algo_3":
            qlist = ht.Algo_3(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        # Update qlist
        if t > ITER*6/10: #Throwing away the first 60%
            #tau = t-ITER*6/10
            #qavg = ht.updateQavg(qlist, qavg, tau)
            # Update the total average queue length
            #epsilon_times_qavg = (1 - S) * qavg # epsilon = (1 - S)
            plotlistx.append(qlist[0])
            plotlisty.append(qlist[2])
            plotlistz.append(qlist[3])
    return [policy, plotlistx, plotlisty, plotlistz] # Return S and its corresponding average queue length

def main(args):
    for Vs in VLIST:
        num_cores = mp.cpu_count()
        Plot_lists = Parallel(n_jobs = num_cores)(delayed(get_Plot_lists)(Vs, policy, 0.99) for policy in PLIST)
        #S_qavg_lists = sorted(S_qavg_lists, key = lambda sub: sub[0])
        policies = [sublist[0] for sublist in Plot_lists] # a list of policies
        # a list of S values in ascending order
        xs = [sublist[1] for sublist in Plot_lists] # a list of lists of q11 lengths
        # a list of qavg values whose order follows the corresponding S value's
        # order
        ys = [sublist[2] for sublist in Plot_lists] # a list of lists of q12 lengths
        # a list of epsilon times qavg values whose order follows the corresponding S value's
        # order
        zs = [sublist[3] for sublist in Plot_lists] # a list of lists of q21 lengths
        with open(str(Vs) + '.csv', 'a', newline = '') as out:
            csvout = csv.writer(out)
            #if PLIST.index(policy) == 0:
                #csvout.writerow([''] + [''] + S_headers)
            for i in range(len(policies)):
                csvout.writerow([policies[i]] + ['xs'] + xs[i])
                csvout.writerow([''] + ['ys'] + ys[i])
                csvout.writerow([''] + ['zs'] + zs[i])
        # Write the traffic intensity values and their corresponding total
        # average queue length and (1-S)*qavg in different policies, each file for one
        # set of V values

if __name__ == "__main__":
    import sys
    main(sys.argv)



