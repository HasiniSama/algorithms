#link : https://www.hackerrank.com/challenges/game-of-stones-1/problem

import os

def gameOfStones(n):
    array = ["L", "L", "W", "W"]

    for i in range(4, n + 1):
        if (array[i - 2] == "L" or array[i - 3] == "L" or array[i - 5] == "L"):
            array.append("W")
        else:
            array.append("L")

    if (array[n] == "W"):
        return "First"
    else:
        return "Second"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
