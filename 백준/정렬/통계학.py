import sys
from collections import Counter
N=int(sys.stdin.readline())
arr = []

for _ in range(N):
    arr.append(int(sys.stdin.readline()))
    
arr.sort()
#산술평균,중앙값, 최빈값, 범위
print(round(sum(arr)/N))
print(arr[N//2])

k=Counter(arr).most_common()

if len(arr) > 1:
    # 같을경우 두번쨰 수 출력
    if k[0][1] == k[1][1]:
        print(k[1][0])
    # 같지않으면 첫번째수 
    else : print(k[0][0])
 
else : 
    print(arr[0]) 
    
print(arr[-1] - arr[0])
