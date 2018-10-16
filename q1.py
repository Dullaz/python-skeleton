# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np
# modify this function, and create other functions below as you wish


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
    offset = 0
    n = 15
    while(True):
        if(portf[0] < 2**n):
            n -= 1
        else:
            break
    while(True):
        offs = 2**n
        if(portf[-1] > offs):
            portf[:] = [x - offs for x in portf]
            n = n - 1
        else:
            break

    # strip away the leading one here
        # print(portf)
        # find the first value that falls below 2**(n)
    i = 0
    for i in range(0, len(portf)):
        if(portf[i] < 2**n):
            break
    # split the arrays in two, higher values on one side, lower values on one side
    portlow = portf[i:]
    porthigh = portf[:i]
    # print(portlow)
    # print(porthigh)
    # start testing
    maxmerge = 0
    if(len(portlow) > len(porthigh)):
        portn = porthigh
        porth = portlow
    else:
        portn = portlow
        porth = porthigh

    maxmerge = 0
    for i in range(len(portn)):
        for j in range(len(porth)):
            temp = portn[i] ^ porth[j]
            if(temp > maxmerge):
                maxmerge = temp
    return maxmerge
