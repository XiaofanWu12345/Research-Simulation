# All functions
import scipy.stats as st
import random
import math

#Returns a list of random variables of arrival rates -- lambda 11, 22, 12 & 21
#The lambdas' values are corresponding v values (the boundary) time traffic intensity s
def arrivalRate(v11, v22, v12, v21, s):
    lambda11 = v11 * s
    lambda22 = v22 * s
    lambda12 = v12 * s
    lambda21 = v21 * s
    lambdaRv_list = [lambda11, lambda22, lambda12, lambda21]
    return lambdaRv_list

#Returns a list of updated queue length after applying the Max Weight Algorithm
#The order of the queue length values in the list is queue11, queue22, queue12, queue21
def MaxWt(q11, q22, q12, q21, lambda11, lambda22, lambda12, lambda21):
    l11 = 0
    l22 = 0
    l12 = 0
    l21 = 0  # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda22:
        l22 = 1
        q22 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1 #Update queue lengths and actual arrivals
    if (q12 + q21) > (q11 + q22):
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        q11 = max([q11 - 1, 0])
        q22 = max([q22 - 1, 0])
    qlist = [q11, q22, q12, q21]
    #print('MaxWt:', 'q11 =', q11, ', q22 =', q22, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l22 =', l22, ', l12 =', l12, ', l21 =', l21)
    return qlist

#Take the queue lengths as parameters and find the match with the maximum size.
#Return 1 if match11_22 has maximum size, 2 for match_12_21, 0 if both matches
#have the same size
def get_MaxSize(q11, q22, q12, q21):
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
#The order of the queue length values in the list is queue11, queue22, queue12, queue21
def MaxSize_random(q11, q22, q12, q21, lambda11, lambda22, lambda12, lambda21):
    l11 = 0
    l22 = 0
    l12 = 0
    l21 = 0  # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda22:
        l22 = 1
        q22 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1
        #Update queue lengths and actual arrivals
    match = get_MaxSize(q11, q22, q12, q21) # Get the match with maximum size
    if match == 1:
        q11 = max([q11 - 1, 0])
        q22 = max([q22 - 1, 0])
    elif match == 2:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        if random.random() < 0.5: # Break ties randomly when both matches share same size
            q11 = max([q11 - 1, 0])
            q22 = max([q22 - 1, 0])
        else:
            q12 = max([q12 - 1, 0])
            q21 = max([q21 - 1, 0])
    qlist = [q11, q22, q12, q21]
    #print('MaxSize_random:', 'q11 =', q11, ', q22 =', q22, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l22 =', l22, ', l12 =', l12, ', l21 =', l21)
    return qlist

# Select the match with maximum size, if two matches are equal in size, select
# match 1 (q11_q22).
#Returns a list of updated queue length
#The order of the queue length values in the list is queue11, queue22, queue12, queue21
def MaxSize_Pri11_22(q11, q22, q12, q21, lambda11, lambda22, lambda12, lambda21):
    l11 = 0
    l22 = 0
    l12 = 0
    l21 = 0  # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda22:
        l22 = 1
        q22 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1
        # Update queue lengths and actual arrivals
    match = get_MaxSize(q11, q22, q12, q21) # Get the match with maximum size
    if match == 2:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        q11 = max([q11 - 1, 0])
        q22 = max([q22 - 1, 0])
    qlist = [q11, q22, q12, q21]
    #print('MaxSize_Pri11_22:', 'q11 =', q11, ', q22 =', q22, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l22 =', l22, ', l12 =', l12, ', l21 =', l21)
    return qlist

# Select the match with maximum size, if two matches are equal in size, select
# the match with maximum weight.
#Returns a list of updated queue length
#The order of the queue length values in the list is queue11, queue22, queue12, queue21
def MaxSize_PriMaxWt(q11, q22, q12, q21, lambda11, lambda22, lambda12, lambda21):
    l11 = 0
    l22 = 0
    l12 = 0
    l21 = 0  # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda22:
        l22 = 1
        q22 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1
        # Update queue lengths and actual arrivals
    match = get_MaxSize(q11, q22, q12, q21) # Get the match with maximum size
    if match == 1:
        q11 = max([q11 - 1, 0])
        q22 = max([q22 - 1, 0])
    elif match == 2:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        if (q12 + q21) > (q11 + q22):
            q12 = max([q12 - 1, 0])
            q21 = max([q21 - 1, 0])
        else:
            q11 = max([q11 - 1, 0])
            q22 = max([q22 - 1, 0])
    qlist = [q11, q22, q12, q21]
    #print('MaxSize_PriMaxWt:', 'q11 =', q11, ', q22 =', q22, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l22 =', l22,  ', l12 =', l12, ', l21 =', l21)
    return qlist

# Select the match with maximum size, if two matches are equal in size, select
# the match with maximum log(weight+1).
#Returns a list of updated queue length
#The order of the queue length values in the list is queue11, queue22, queue12, queue21
def MaxSize_PriMaxWtLog(q11, q22, q12, q21, lambda11, lambda22, lambda12, lambda21):
    l11 = 0
    l22 = 0
    l12 = 0
    l21 = 0  # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda22:
        l22 = 1
        q22 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1
        # Update queue lengths and actual arrivals
    match = get_MaxSize(q11, q22, q12, q21) # Get the match with maximum size
    if match == 1:
        q11 = max([q11 - 1, 0])
        q22 = max([q22 - 1, 0])
    elif match == 2:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        if math.log(q12 + q21 + 1) > math.log(q11 + q22 + 1):
            q12 = max([q12 - 1, 0])
            q21 = max([q21 - 1, 0])
        else:
            q11 = max([q11 - 1, 0])
            q22 = max([q22 - 1, 0])
    qlist = [q11, q22, q12, q21]
    #print('MaxSize_PriMaxWt:', 'q11 =', q11, ', q22 =', q22, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l22 =', l22,  ', l12 =', l12, ', l21 =', l21)
    return qlist

# Select the match with maximum size, if two matches are equal in size, select
# the match with minimum weight.
#Returns a list of updated queue length
#The order of the queue length values in the list is queue11, queue22, queue12, queue21
def MaxSize_PriMinWt(q11, q22, q12, q21, lambda11, lambda22, lambda12, lambda21):
    l11 = 0
    l22 = 0
    l12 = 0
    l21 = 0  # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda22:
        l22 = 1
        q22 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1
        # Update queue lengths and actual arrivals
    match = get_MaxSize(q11, q22, q12, q21) # Get the match with maximum size
    if match == 1:
        q11 = max([q11 - 1, 0])
        q22 = max([q22 - 1, 0])
    elif match == 2:
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        if (q12 + q21) < (q11 + q22):
            q12 = max([q12 - 1, 0])
            q21 = max([q21 - 1, 0])
        else:
            q11 = max([q11 - 1, 0])
            q22 = max([q22 - 1, 0])
    qlist = [q11, q22, q12, q21]
    #print('MaxSize_PriMinWt:', 'q11 =', q11, ', q22 =', q22, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l22 =', l22, ', l12 =', l12, ', l21 =', l21)
    return qlist

#Select the match with larger actual arrivals
#If two matches share the same total sum of actual arrivals, give priority to the match with max weight
#Returns a list of updated queue length
#The order of the queue length values in the list is queue11, queue22, queue12, queue21
def MaxArrival_PriMaxWt(q11, q22, q12, q21, lambda11, lambda22, lambda12, lambda21):
    l11 = 0
    l22 = 0
    l12 = 0
    l21 = 0  # Actual arrivals
    if random.random() < lambda11:
        l11 = 1
        q11 += 1
    if random.random() < lambda22:
        l22 = 1
        q22 += 1
    if random.random() < lambda12:
        l12 = 1
        q12 += 1
    if random.random() < lambda21:
        l21 = 1
        q21 += 1
        # Update queue lengths and actual arrivals
    if (l11 + l22) > (l12 + l21):
        q11 = max([q11 - 1, 0])
        q22 = max([q22 - 1, 0])
    elif (l11 + l22) < (l12 + l21):
        q12 = max([q12 - 1, 0])
        q21 = max([q21 - 1, 0])
    else:
        if (q12 + q21) > (q11 + q22):
            q12 = max([q12 - 1, 0])
            q21 = max([q21 - 1, 0])
        else:
            q11 = max([q11 - 1, 0])
            q22 = max([q22 - 1, 0])
    qlist = [q11, q22, q12, q21]
    #print('MaxArrival_PriMaxWt:', 'q11 =', q11, ', q22 =', q22, ', q12 =', q12, ', q21 =', q21, ', l11 =', l11, ', l22 =', l22, ', l12 =', l12, ', l21 =', l21)
    return qlist


#Returns the updated average of the total queue length for the current time slot
def updateQavg(qlist, qavg, tau):
    return qavg*(tau-1)/tau + sum(qlist)/tau