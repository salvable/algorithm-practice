from bisect import bisect_left, bisect_right
import sys


n = int(input())
A = list(map(int,sys.stdin.readline().split()))
m = int(input())
B = list(map(int,sys.stdin.readline().split()))

A.sort()

for i in B:
    index = bisect_left(A,i)
    index2 = bisect_right(A,i)

    print(index2 - index, end= " ")
