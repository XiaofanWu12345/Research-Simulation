# Main Loop
import Functions as ht #ht for heavy traffic
import scipy.stats as st
import csv
import matplotlib.pyplot as plt
from joblib import Parallel, delayed
import multiprocessing as mp

VLIST = [[1/2, 1/2, 1/2], [3/4, 1/4, 1/4], [0.6,0.4,0.4]]
#a list of lists whose elements are the values of v in the order of v11, v12, v21
#SLIST = [s/10 for s in range(1,10)] + [s/100 for s in range(91,100)]
SLIST = [s/100 for s in range(91,100)]
# a list iof traffic intensity values from 0.1, 0.2 to 0.9, 0.91 to 0.99
PLIST = ["MaxWt", "PriC", "PriE"]
# a list of selection policies

ITER = 100000
#time length of simulation

Total_figures = [] #Initialize the list to store data for the 3 figures
# for 3 set of V values

def get_S_qavg_lists(Vs, policy, S):
    qavg = 0
    qlist = [0, 0, 0] # a list for values of the average queue length
    # in the order of q11, q12, q21
    for t in range(1, ITER + 1):
        lambdaRv_list = ht.arrivalRate(Vs[0], Vs[1], Vs[2], S)
        # a list for random variables of the arrival rate, normal distr
        # in the order of lambda11_norm, lambda12_norm, lambda21_norm
        if policy == "MaxWt":
            qlist = ht.MaxWt(qlist[0], qlist[1], qlist[2],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2])
        elif policy == "PriC":
            qlist = ht.PriC(qlist[0], qlist[1], qlist[2],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2])
        elif policy == "PriE":
            qlist = ht.PriE(qlist[0], qlist[1], qlist[2],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2])
        # Update qlist
        if t > ITER/10:
            tau = t-ITER/10
            qavg = ht.updateQavg(qlist, qavg, tau)
        # Update the total average queue length
    return [S, qavg] # Return S and its corresponding average queue length

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
            figure_list = [S_headers, qavg_values]
            Total_figures.append(figure_list)
            # Add the S_headers and qavg_values to the Total_figures list to store
            # the x-axis and y-axis data for the figure of current V value and
            # policy combination
            with open(str(Vs) + '.csv', 'a', newline = '') as out:
                csvout = csv.writer(out)
                if PLIST.index(policy) == 0:
                    csvout.writerow([''] + S_headers)
                csvout.writerow([policy] + qavg_values)
            # Write the traffic intensity values and their corresponding total
            # average queue length in seperate csv files, each file for one
            # combination of V values and loading policy

    # The loops to generate 3 figures
    for f in range(0,3): # f means the figure's number, which represents the set of
    # V values in use. f is the set's order in VLIST
        plt.figure(f + 1)
        for i in range(0,3):
        # i controls the policy in use, the policy's order in PLIST
            plt.plot(Total_figures[3 * f + i][0], Total_figures[3 * f + i][1],
                    label = PLIST[i], linewidth = 4 if i == 0 else 2,
                    markersize = 12 )
        plt.xlabel('Traffic Intnesity')
        plt.ylabel('Average Total Queue Length -- E[Q11 + Q12 + Q21]')
        plt.title('E[Q11 + Q12 + Q21] vs Traffic Intensity, Vs Value: '
                + str(VLIST[f]))
        plt.grid(True)
        plt.legend()
        plt.savefig("Avg_q_Vs " + str(VLIST[f]) + ".png")
        plt.savefig("Avg_q_Vs " + str(VLIST[f]) + ".eps")
        plt.savefig("Avg_q_Vs " + str(VLIST[f]) + ".svg")
        plt.show()

if __name__ == "__main__":
    import sys
    main(sys.argv)



