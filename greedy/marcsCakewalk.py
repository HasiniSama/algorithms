#link : https://www.hackerrank.com/challenges/marcs-cakewalk/problem

n = int(input().strip())
arr = sorted(map(int, input().rstrip().split()),reverse=True)
sum = 0
for i in range(0,n):
    sum += pow(2,i) * arr[i]
print(sum)

"""
print(sum(c * 2 ** j for (j, c) in enumerate(sorted(map(int, input().split()), reverse=True))))

reverse=True - in descending order
enumerate() - adds a counter to an iterable and returns it in a form of enumerating object
sum() - adds
"""
