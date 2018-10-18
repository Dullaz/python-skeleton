# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

#compute all combinations for two portfolios
def question04(rows, numberMachines):
  # modify and then return the variable below
  minn = 100000
  tempmin = 100000
  innermin = 100000
  print(rows)
  print(numberMachines)
  for i in rows:
    tempmin = 100000
    for j in range(len(i) - numberMachines+1):
      innermin = 0
      for k in range(numberMachines):
        if(i[j+k] == 'X'):
           innermin = 100000
           break;
        innermin += i[j+k]
      if(innermin < tempmin):
           tempmin = innermin
    if(tempmin < minn):
           minn=tempmin
  answer = minn
  return answer
