#!/bin/python3
# MARVIN BANTON

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    store = {}
    res = 0
    for num in arr:
        store[num] = 1
        if num + k in store:
            res += 1
        if num -k in store:
            res += 1
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
