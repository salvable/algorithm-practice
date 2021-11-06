def solution(files):
    answer = []
    
    for file in files:
        # file을 head, number, tail로 나눔
        head, number, tail = "", "", ""
        
        # 숫자를 탐색하기위한 플래그
        check = False
        for i in range(len(file)):
            # 숫자면 
            if file[i].isdigit() :
                number += file[i]
                check = True
            
            # 숫자가 나오기 전
            elif not check:
                head += file[i]
            # 나머지 문자는 tail에 넣고 반복문 탈출
            else:
                tail = file[i:]
                break
                
        answer.append((head,number,tail))
    
    # head를 기준으로 sort하고 같을경우 number를 기준으로 정렬
    answer.sort(key = lambda x : (x[0].upper(),int(x[1])))
    
    return ["".join(i) for i in answer]
