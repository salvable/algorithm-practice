def solution(str1, str2):
    
    #소문자 변환
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_list = []
    str2_list = []
    
    
    # 두 글자씩 끊어서 그것이 알파벳으로 이루어져있다면 리스트에 저장하여 구함
    for i in range(len(str1)-1):
        string = str1[i]+str1[i+1]
        if string.isalpha():
            str1_list.append(string)
    
    for i in range(len(str2)-1):
        string = str2[i]+str2[i+1]
        if string.isalpha():
            str2_list.append(string)

    #교집합 배열 구함    
    intersection = [str2_list.remove(s) for s in str1_list if s in str2_list]
    

    #교집합, 합집합 둘다 0이면 65536 리턴
    if len(intersection) == 0 and len(str1_list)+ len(str2_list) == 0:
        return 65536
    
    
    return int(len(intersection) / (len(str1_list)+ len(str2_list)) * 65536)
