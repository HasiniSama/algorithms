#link : https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem

def maximumPerimeterTriangle(sticks):
    i = len(sticks) - 3
    result = []

    while i >=0 and (sticks[i] + sticks[i+1] <= sticks[i+2]):
        i -= 1

    if i >= 0:
        return([sticks[i],sticks[i+1],sticks[i+2]])
    else:
        return([-1])

n = int(input().strip())
sticks = sorted(list(map(int, input().rstrip().split())))
print(*maximumPerimeterTriangle(sticks))
