n = int(input())

triangle = []

for _ in range(n):
    triangle.append(list(map(int, input().split())))


for i in range(1,n):
    for j in range(i+1):
        # 각 줄의 첫번쨰 원소인 경우 받는 숫자는 각 열의 첫번째로 고정되어 있으므로
        if j == 0:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j]
        # 각 줄의 마지막 원소는 이전 열의 마지막으로 고정
        elif j == i:
            triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
        # 중간에 있는 숫자들은 이전줄 j, j-1과 비교하여 더 큰 값을 사용함
        else:
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j], triangle[i][j] + triangle[i-1][j-1])


print(max(triangle[n-1]))
