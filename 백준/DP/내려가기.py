import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
# 메모리 이슈로 배열 하나먼저 받고 반복문 돌 때 입력받음, 슬라이
graph = list(map(int, input().split()))

max_arr = graph
min_arr = graph

for i in range(n-1):
    x, y, z = map(int, input().split())
    max_arr = [x + max(max_arr[0], max_arr[1]), y + max(max_arr), z + max(max_arr[1], max_arr[2])]
    min_arr = [x + min(min_arr[0], min_arr[1]), y + min(min_arr), z + min(min_arr[1], min_arr[2])]

print(max(max_arr), min(min_arr))

