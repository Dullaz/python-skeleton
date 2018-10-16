# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below as you wish
def question01(portfolios):
  # modify and then return the variable below
  
  answer = solve(portfolios)
  return answer

def solve(portf):
  #Sort descending
  portf.sort(reverse=True)
  #Check for 0, if true return highest number
  if(portf[-1] == 0):
	  return portf[0]
  #Strip MSBs if all values are above 2**(n-1)
  offset = 0
  n=15
  while(True):
    if(portf[0] < 2**n):
      n-=1
    else:
      break
  while(True):
    if(portf[-1] > 2**n):
      offset += 2**n #store the offset we stripped away
      n -= 1
    else:
      break
    
  #strip away the leading one here
  if(offset > 0):
    portf[:] = [x - offset for x in portf]
  
  #find the first value that falls below 2**(n)
  i=0
  for i in range(0,len(portf)):
    if(portf[i] < 2**n):
      break
  #split the arrays in two, higher values on one side, lower values on one side
  portlow = portf[i:]
  porthigh = portf[:i]
  
  #start testing
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

  '''
  for i in range(len(portn)):
	  tempm = modbin((portn[i]^2**n),porth,n)
	  if(tempm > maxmerge):
		  maxmerge = tempm
  return(maxmerge + offset)
  
def modbin(needle,haystack,n):
	first=0
	last = len(haystack)-1
	found =false
	while first<=last:
		midpoint = (first+last)//2
		if haystack[midpoint] == needle:
			return (2**n)
		else:
			if needle < haystack[midpoint]:
				last = midpoint -1
			else:
				first = midpoint + 1
	return max(origin^haystack[first],origin^haystack[last])
  '''

#print(question01([9,7,12,2]))
