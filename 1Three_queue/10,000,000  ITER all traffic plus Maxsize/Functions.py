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

#Take the queue lengths as parameters and find the match with the maximum size.
#Return 1 if match11_22 has maximum size, 2 for match_12_21, 0 if both matches
#have the same size
def get_MaxSize(q11, q12, q21):
    q22 = 0
    match11_22 = 0
    match12_21 = 0 #Initialize the size of each match
    for q in [q11, q22]:
        if q > 0:
            match11_22 +=1
    for q in [q12, q21]:
        if q > 0:
            match12_21 +=1 #Update the size of each match
    if match11_22 > match12_21:
        return 1
    elif match12_21 > match11_22: #Find the match with maximum size
        return 2
    else:
        return 0

# Select the match with maximum size, if two matches are equal in size, select
# a match randomly with 0.5 propbability
#Returns a list of updated queue length
#The order of the queue length values in the list is queue11, queue12, queue21
def MaxSize_random(q11, q12, q21, lambda11, lambda12, lambda21):
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
        #Update queue lengths and actual arrivals
    match = get_MaxSize(q11, q12, q21) # Get the match with maximum size
    if match == 1:
        q11 = max([q11 - 1, 0])
    elif match == 2:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        if random.random() < 0.5: # Break ties randomly when both matches share same size
            q11 = max([q11 - 1, 0])
        else:
            q12 = max([q12 - 1, 0])
            q21 = max([q21 - 1, 0])
    qlist = [q11, q12, q21]
    #print('MaxSize_random:', 'q11 =', q11, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l12 =', l12, ', l21 =', l21)
    return qlist

# Select the match with maximum size, if two matches are equal in size, select
# the match with maximum weight.
#Returns a list of updated queue length
#The order of the queue length values in the list is queue11, queue12, queue21
def MaxSize_PriMaxWt(q11, q12, q21, lambda11, lambda12, lambda21):
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
        # Update queue lengths and actual arrivals
    match = get_MaxSize(q11, q12, q21) # Get the match with maximum size
    if match == 1:
        q11 = max([q11 - 1, 0])
    elif match == 2:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        if (q12 + q21) > q11:
            q12 = max([q12 - 1, 0])
            q21 = max([q21 - 1, 0])
        else:
            q11 = max([q11 - 1, 0])
    qlist = [q11, q12, q21]
    #print('MaxSize_PriMaxWt:', 'q11 =', q11, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l12 =', l12, ', l21 =', l21)
    return qlist

#Returns the updated average of the total queue length for the current time slot
def updateQavg(qlist, qavg, tau):
    return qavg*(tau-1)/tau + sum(qlist)/tau