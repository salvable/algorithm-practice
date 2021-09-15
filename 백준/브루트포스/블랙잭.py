# 카드의 개수와 주어진 M의 값
n,m= map(int,input().split())
# 카드 리스트
card =list(map(int,input().split()))
card.sort()

answer = 0

for i in range(0,len(card)-2):
    for j in range(i+1,len(card)-1):
        for z in range(j+1,len(card)):
            result = card[i] + card[j] + card[z]

            if result > m:
                continue

            else:
                answer = max(answer,result)


print(answer)
