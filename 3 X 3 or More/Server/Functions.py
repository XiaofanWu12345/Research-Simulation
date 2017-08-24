# All functions
import scipy.stats as st
import random
import numpy as np
from scipy.optimize import linear_sum_assignment
import math

#Initialize the Vs list and the matrix representing the queues for the
#combinations of inputs and outputs of the switch
def initializeMatrix(n):
    Vs = [[1/n for i in range(n)] for k in range(n)]
    Queues = np.array([[0 for i in range(n)] for k in range(n)])
    return [Vs, Queues]

#Returns a list of actual arrival rates -- lambdas
#The lambdas' values are corresponding v values (the boundary) time traffic intensity s
def arrivalRate(Vs, s):
    lambdaRv_list = np.array([[V*s for V in Vsublist] for Vsublist in Vs])
    return lambdaRv_list

# Update queue lengths according to corresponding arrival rates
def updateQ(Queues, lambdaRv_list):
    for i in range(len(Queues)):
        for j in range(len(Queues[i])):
            if random.random() < lambdaRv_list[i,j]:
                Queues[i,j] += 1
    #Update queue lengths and actual arrivals
    return Queues

#Returns a matrix of updated queue length after applying the Max Weight Algorithm
def MaxWt(Queues):
    Queuesdiff = -Queues
    #a new matrix of negative queue lengths
    row_ind, col_ind = linear_sum_assignment(Queuesdiff)
    #apply the Hungarian algorithm to select the rows and corresponding colums
    #with minimus sum of values in total
    for i in range(len(row_ind)):
        row = row_ind[i]
        col = col_ind[i]
        if Queues[row,col] >= 1:
            Queues[row,col] -= 1
        else:
            Queues[row,col] = 0
    #update the queue lengths of the selected combinations with max weight
    return Queues

#Returns a matrix of updated queue length after applying the MaxSize_random Algorithm
def MaxSize_random(Queues):
    Queuesdiff = np.array([[1 if k > 0 else 0 for k in sublist] for sublist in Queues])
    row_ind, col_ind = linear_sum_assignment(-Queuesdiff)
    for i in range(len(row_ind)):
        row = row_ind[i]
        col = col_ind[i]
        if Queues[row,col] >= 1:
            Queues[row,col] -= 1
        else:
            Queues[row,col] = 0
    return Queues

#Returns a matrix of updated queue length after applying the MaxSize_PriMaxWt Algorithm
def MaxSize_PriMaxWt(Queues):
    T = len(Queues) * max([max(sub) for sub in Queues])
    Queuesdiff = np.array([[T + k if k > 0 else 0 for k in sublist] for sublist in Queues])
    row_ind, col_ind = linear_sum_assignment(-Queuesdiff)
    for i in range(len(row_ind)):
        row = row_ind[i]
        col = col_ind[i]
        if Queues[row,col] >= 1:
            Queues[row,col] -= 1
        else:
            Queues[row,col] = 0
    return Queues

#Returns a matrix of updated queue length after applying the MaxSize_PriMaxWtLog Algorithm
def MaxSize_PriMaxWtLog(Queues):
    Queueslog = np.array([[math.log(q+1) for q in sub] for sub in Queues])
    T = len(Queueslog) * max([max(sub) for sub in Queueslog])
    Queuesdiff = np.array([[T + k if k > 0 else 0 for k in sublist] for sublist in Queueslog])
    row_ind, col_ind = linear_sum_assignment(-Queuesdiff)
    for i in range(len(row_ind)):
        row = row_ind[i]
        col = col_ind[i]
        if Queues[row,col] >= 1:
            Queues[row,col] -= 1
        else:
            Queues[row,col] = 0
    return Queues



#Returns the updated average of the total queue length for the current time slot
def updateQavg(Queues, qavg, tau):
    return qavg*(tau-1)/tau + sum(sum(Queues))/tau