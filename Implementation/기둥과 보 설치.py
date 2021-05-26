def confirm(answer):
    for x, y, struct in answer:
        # 구조물이 기둥일 경우
        if struct == 0:
            # 설치된 것이 바닥,                보 위                  , 기둥위인지 확인
            # 보는 오른쪽으로 지어지므로 x-1의 좌표또한 확인해줘야 한다.
            if y == 0 or [x,y,1] in answer or [x-1,y,1] in answer or [x,y-1,0] in answer:
                continue
            # 아니라면 False 리턴
            return False
        
        # 구조물이 보일 경우
        elif struct == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or [x-1,y,1] in answer and [x+1,y,1] in answer:
                continue
            return False
    return True
def solution(n, build_frame):
    answer = []
    
    for frame in build_frame:
        # x축 / y축 / 구조물 / 연산
        x,y,struct,oper = frame
        
        # 건설하는 경우
        if oper == 1:
            answer.append([x,y,struct])
            # 설치가 가능한지 확인
            if not confirm(answer):
                # 가능하지 않으면 answer배열에서 제거해줌
                answer.remove([x,y,struct])
        
        # 제거하는 경우
        if oper == 0:
            answer.remove([x,y,struct])
            # 제거가 가능한지 확인
            if not confirm(answer):
                # 아니라면 answer배열에 다시 넣어줌
                answer.append([x,y,struct])
            
    return sorted(answer)
