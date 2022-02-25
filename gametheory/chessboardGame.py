#link : https://www.hackerrank.com/challenges/a-chessboard-game-1/problem

import os

def chessboardGame(x, y):
    a = x % 4
    b = y % 4

    if ((a == 1 or a == 2) and (b == 1 or b == 2)):
        return "Second"
    return "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])

        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()