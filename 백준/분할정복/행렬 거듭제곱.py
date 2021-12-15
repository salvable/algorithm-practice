n, b = map(int, input().split(" "))

arr = []

def matrix_mult(A, B):
    # n * n 행렬끼리의 곱셈이므로
    n = len(A)
    temp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                temp[i][k] += A[i][j] * B[j][k]
            temp[i][k] %= 1000
    return temp


def matrix_pow(A, n):
    if n == 1:
        return A
    # 짝수인경우 구한 행렬끼리 계산
    if n % 2 == 0:
        temp = matrix_pow(A, n//2)
        return matrix_mult(temp, temp)
    # 홀수인 경우에는 행렬을 하나 떼어 따로 계산해줌
    else:
        temp = matrix_pow(A, n-1)
        return matrix_mult(temp, A)

for _ in range(n):
    arr.append(list(map(int, input().split(" "))))


arr2 = matrix_pow(arr,b)

for i in arr2:
    for j in i:
        print(j%1000, end=" ")
    print("")
