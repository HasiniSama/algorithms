#link : https://www.hackerrank.com/challenges/grid-challenge/problem

t = int(input().strip())
n = int(input().strip())

while t > 0 :
    for i in range(0,n) :
        arr = sorted(list(map(int, input().rstrip().split())))

    t+=1



print(n)
print(t)

#leave for further thinking