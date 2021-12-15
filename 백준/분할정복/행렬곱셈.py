A = []
B = []

N, M = map(int, input().split(" "))

for _ in range(N):
    A.append(list(map(int, input().split(" "))))

M, K = map(int, input().split(" "))

for _ in range(M):
    B.append(list(map(int, input().split(" "))))

answer = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            answer[i][j] += A[i][k] * B[k][j]

for i in answer:
    for j in i:
        print(j, end=" ")
    print("")
