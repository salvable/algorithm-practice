def solution(n):
    bit = bin(n)
    
    #0bXXXXXXX 이므로 인덱싱 따로 안하고 1 개수 카운트
    one_count = bit.count("1")
    
    while True:
        n += 1
        temp = bin(n)
        
        if(temp.count("1") == one_count):
            break

    return n
