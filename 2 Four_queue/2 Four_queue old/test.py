#Test
import Functions as ht #ht for heavy traffic
import scipy.stats as st
SLIST = [s/10 for s in range(1,10)] + [s/100 for s in range(91,100)]
#SLIST = [s/100 for s in range(91,100)]
# a list iof traffic intensity values from 0.1, 0.2 to 0.9, 0.91 to 0.99
PLIST = ["MaxWt", "MaxSize_random", "MaxSize_Pri11_22", "MaxSize_PriMaxWt", "MaxSize_PriMinWt", "MaxArrival_PriMaxWt"]
ITER = 100
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
        elif policy == "MaxSize_random":
            qlist = ht.MaxSize_random(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        elif policy == "MaxSize_Pri11_22":
            qlist = ht.MaxSize_Pri11_22(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        elif policy == "MaxSize_PriMaxWt":
            qlist = ht.MaxSize_PriMaxWt(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        elif policy == "MaxSize_PriMinWt":
            qlist = ht.MaxSize_PriMinWt(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])
        elif policy == "MaxArrival_PriMaxWt":
            qlist = ht.MaxArrival_PriMaxWt(qlist[0], qlist[1], qlist[2], qlist[3],
                    lambdaRv_list[0], lambdaRv_list[1],
                    lambdaRv_list[2], lambdaRv_list[3])

for policy in PLIST:
    for S in SLIST:
        get_S_qavg_lists([1/2, 1/2, 1/2, 1/2], policy, S)


