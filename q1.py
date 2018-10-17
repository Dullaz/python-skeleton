import numpy as np
# modify this function, and create other functions below as you wish
from time import clock


def question01(portfolios):
    # modify and then return the variable below
    answer = solve(portfolios)
    return answer


def solve(portf):
    # Sort descending
    maxmerge = 0
    
    for i in range(len(portf)):
        for j in range(i,len(portf)):
            temp = portf[i]^portf[j]
            if(temp > maxmerge):
                maxmerge = temp
    return maxmerge
