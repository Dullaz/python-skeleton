import numpy as np
# modify this function, and create other functions below as you wish
from time import clock


def question01(portfolios):
    # modify and then return the variable below
    answer = solve(portfolios)
    return answer


def solve(portf):
    # Sort descending
    portf.sort(reverse=True)
    if(len(portf) == 0):
        return 0
    if(portf[-1] == 0):
        return portf[0]
    # Strip MSBs if all values are above 2**(n-1)
    n = 30
    while(True):
      for i in range(len(portf)):
        if(portf[i] < 2**n):
          break
      n -= 1

    
    # split the arrays in two, higher values on one side, lower values on one side
    portlow = portf[i:]
    porthigh = portf[:i]
    # print(portlow)
    # print(porthigh)
    # start testing
    #maxmerge = 0
    '''if(len(portlow) > len(porthigh)):
        portn = porthigh
        porth = portlow
    else:
        portn = portlow
        porth = porthigh
'''
    maxmerge = 0
    for i in range(len(portn)):
        for j in range(len(porth)):
            temp = portn[i] ^ porth[j]
            if(temp > maxmerge):
                maxmerge = temp
    return maxmerge
