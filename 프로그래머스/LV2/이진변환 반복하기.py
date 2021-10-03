def solution(s):  
    count1 = 0
    count2 = 0
    
    while True:
        if s == "1":
            break
         
        count1 += s.count("0")
        s = s.replace("0","")
        
        s = bin(s.count("1"))[2:]
        count2 += 1

    return [count2,count1]
