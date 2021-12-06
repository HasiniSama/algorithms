#link : https://www.hackerrank.com/challenges/luck-balance/problem

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


n, k = map(int, input().split())
contests = [list(map(int, input().split())) for _ in range(n)]
print(luckBalance(k, contests))
