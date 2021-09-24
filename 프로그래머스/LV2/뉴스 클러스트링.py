def solution(str1, str2):
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_Array = []
    str2_Array = []

    for i in range(len(str1) -1):
        temp = str1[i] + str1[i+1]
        if temp.isalpha():
            str1_Array.append(temp)
            
    for i in range(len(str2) -1):
        temp = str2[i] + str2[i+1]
        if temp.isalpha():
            str2_Array.append(temp)
           
    # 교집합을 구하는 배열
    intersaction = []
    
    for i in str1_Array:
        if i in str2_Array:
            intersaction.append(i)
            str2_Array.remove(i)
            
    if len(str1_Array) == 0 and len(str2_Array) == 0:
        return 1 * 65536

    return int(len(intersaction) / (len(str1_Array) + len(str2_Array)) * 65536)
