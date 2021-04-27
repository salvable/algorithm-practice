def solution(s):  
    zero_remove_count = 0
    binary_count = 0
    
    while True:
        if(s == "1"):
            break
        zero_remove_count += s.count('0')
        s = s.replace("0","")
    
        s = bin(len(s))[2:]
        binary_count += 1
        
    return [binary_count,zero_remove_count]
