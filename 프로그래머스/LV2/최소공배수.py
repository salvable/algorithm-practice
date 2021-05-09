# gcd는 최소공약수 모듈
from math import gcd

def solution(arr):
    answer = 0
    
    
    # 최소 공배수를 담을 배열
    temp = 0
    
    for i in range(len(arr)-1):
        # 첫번째 계산이라면 최소 공배수를 먼저 구해줘야 함
        if i == 0:  
            temp = arr[i] * arr[i+1] // gcd(arr[i],arr[i+1])
        # 첫번째가 아닐경우 최소공배수를 구한값을 활용하여 구해줌
        else:
            temp = temp * arr[i+1] // gcd(temp,arr[i+1])
    return temp
