#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    
    pm_am = s[-2]
    if pm_am == 'A':
        return ("0" + str(int(s[0:2]) % 12) + s[2:-2])
    else:
        return (str(int(s[0:2]) % 12 + 12) + s[2:-2])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
