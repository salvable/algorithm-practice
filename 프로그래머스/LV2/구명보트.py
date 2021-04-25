import collections

def solution(people, limit):
    
    people.sort()
    
    people = collections.deque(people)
    
    answer = 0
    
    #queue 안에 사람이 남아있으면
    while(people):
        # 남은 사람이 한명일시 멈춤
        if(len(people) == 1):
            answer += 1
            break
        # 무게 초과시  제일 무거운 사람 한명만 뻄
        if(people[0] + people[-1] > limit):
            people.pop()
            answer += 1
        # 무게 초과가 아닐시 처음과 끝 두명 뻄
        else:
            people.pop()
            people.popleft()
            answer += 1
    
    return answer
