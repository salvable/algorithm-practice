
def confirm(answer):
    for x,y,struct in answer:    
        # 설치할 구조물이 기둥인경우 
        if struct == 0:
            # y좌표가 바닥 or 다른 기둥 위 or 보 위
            if y == 0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            else:
                return False
        # 설치할 구조물이 보인경우
        else:
            # 한쪽 끝부분이 기둥 위에 있거나 양쪽으로 다른 보와 연결될 때 
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or [x-1,y,1] in answer and [x+1,y,1] in answer:
                continue
            else:
                return False
    return True
         
         
def solution(n, build_frame):
    answer = []
    
    for i in build_frame:
        # 각각은 x,y 좌표, 구조물, 삽입 or 제거
        x,y,struct,oper = i
        
        # 설치하는경우
        if oper == 1:
            # 구조물을 추가하고
            answer.append([x,y,struct])
            # 추가한 구조물이 올바르지 않다면
            if confirm(answer) == False:
                answer.remove([x,y,struct])
        else:
            answer.remove([x,y,struct])
            if confirm(answer) == False:
                answer.append([x,y,struct])
            
    return sorted(answer) 
