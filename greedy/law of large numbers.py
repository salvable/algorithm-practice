#n개의 수 를 입력받고 M번 더하고 K번 반복 가능 
n,m,k = map(int, input().split())

#n개의 개수 만큼 data를 입력해주어야 함
print("n 개의 개수 만큼 data를 입력해주세요: ")
data = list(map(int,input().split()))

answer = 0
k_count = 0
if(len(data) != n):
    print("n의 개수를 확인하세요")
else:
    data.sort(reverse = True)
    print(data)

    first = data[0]
    second = data[1]

    for i in range(m):
        
        if( k_count == k):
            answer += second
            k_count = 1

        else:
            answer += first
            k_count += 1
print(answer)
