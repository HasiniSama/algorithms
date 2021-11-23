# link : https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

n = int(input().strip())
arr = sorted(map(int, input().rstrip().split()))
if len(arr) != len(set(arr)):
    print(0)
else:
    print(min(abs(x-y) for x,y in zip(arr,arr[1:])))

"""
strip() - remove all white spaces
input() - get input from console

rstrip() - remove all white spaces to the right
split() - split the string by white spaces
map(int, ) - map each element to int
sorted() - sort by asecending order

set() - remove all duplicates and make a set
zip() - pair each from the two arrays
abs() - get the absolute value
min() - get the minimum value

arr[1:] - slice notation
"""
