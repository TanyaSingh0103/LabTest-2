import numpy as np
myArr = np.array(['hello', 'my', 'name is', 'Tanya'])

def getShortest(arr):
    minSt = 'xxxxxxx'
    for i in arr:
        if i < minSt:
            minSt = i
    return minSt

def getLongest(arr):
    maxSt = ''
    for i in arr:
        if i > maxSt:
            maxSt = i
    return maxSt if len(maxSt) > 5 else getShortest(arr)

getLongest(myArr)
