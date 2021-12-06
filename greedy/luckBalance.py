#link : https://www.hackerrank.com/challenges/luck-balance/problem

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    sum = 0
    i = 0
    n = len(contests)

    while i < n:
        sum = sum + contests[i][0]
        if (contests[i][1] == 0):
            contests.pop(i)
            i -= 1
            n -= 1
        i += 1

    k = len(contests) - k
    while k > 0:
        x = (contests.index(min(contests)))
        sum -= (contests[x][0] * 2)
        contests.pop(x)
        k -= 1
    return sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
