n = int(input()) 

for i in range(1, n+1):   
    value = sum((map(int, str(i))))  
    result = i + value
    # 가장 작은 생성자를 만났을시 break
    if result == n:
        print(i)
        break
    #같을경우 생성자가 없다.
    if i == n:  
        print(0)
