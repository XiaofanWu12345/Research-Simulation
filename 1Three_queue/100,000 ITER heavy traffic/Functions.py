# All functions
import scipy.stats as st
import random

#Returns a list of random variables of arrival rates -- lambda 11, 12 & 21
#The rvs follow normal distribution whose mean is the corresponding v
#(the boundary) times traffic intensity s, and whose variance is 0.25
def arrivalRate(v11, v12, v21, s):
    lambda11 = v11 * s
    lambda12 = v12 * s
    lambda21 = v21 * s
    lambdaRv_list = [lambda11, lambda12, lambda21]
    return lambdaRv_list

#Returns a list of updated queue length after applying the Max Weight Algorithm
#The order of the queue length values in the list is queue11, queue12, queue21
def MaxWt(q11, q12, q21, lambda11, lambda12, lambda21):
    l11 = 0
    l12 = 0
    l21 = 0 # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1
    if (q12 + q21) > q11:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        q11 = max([q11 - 1, 0])
    qlist = [q11, q12, q21]
    #print('MaxWt:', 'q11 =', q11, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l12 =', l12, ', l21 =', l21)
    return qlist

#Returns a list of updated queue length after applying the Piority C Algorithm
#The order of the queue length values in the list is queue11, queue12, queue21
def PriC(q11, q12, q21, lambda11, lambda12, lambda21):
    l11 = 0
    l12 = 0
    l21 = 0  # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1
    if q11 > 0:
        q11 = max([q11 - 1, 0])
    else:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    qlist = [q11, q12, q21]
    #print('PriC:', 'q11 =', q11, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l12 =', l12, ', l21 =', l21)
    return qlist

#Returns a list of updated queue length after applying the Priority E Algorithm
#The order of the queue length values in the list is queue11, queue12, queue21
def PriE(q11, q12, q21, lambda11, lambda12, lambda21):
    l11 = 0
    l12 = 0
    l21 = 0  # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1
    if q12 > 0 and q21 > 0:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    elif q11 > 0:
        q11 = max([q11 - 1, 0])
	else:
		q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    qlist = [q11, q12, q21]
    #print('PriE:', 'q11 =', q11, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l12 =', l12, ', l21 =', l21)
    return qlist

#Returns the updated average of the total queue length for the current time slot
def updateQavg(qlist, qavg, tau):
    return qavg*(tau-1)/tau + sum(qlist)/tau