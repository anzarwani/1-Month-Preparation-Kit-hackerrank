#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    countP = 0
    countN = 0
    countZ = 0
    
    for i in range(len(arr)):
        if arr[i] < 0:
            countN += 1
        elif arr[i] > 0:
            countP += 1
        else:
            countZ += 1
            
    print("{:.6f}".format(countP/len(arr)))
    print("{:.6f}".format(countN/len(arr)))
    print("{:.6f}".format(countZ/len(arr)))
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
