from itertools import permutations 

def check(user,banned):
    for i in range(len(banned)):
        if len(user[i]) != len(banned[i]):
            return False
        
        for j in range(len(user[i])):
            # * 이면 모두 통과되니 넘어감
            if banned[i][j] == "*":
                continue
            # 해당 문자가 다르면 False
            if banned[i][j] != user[i][j]:
                return False
    # 전부 통과 되면 True 리턴
    return True

def solution(user_id, banned_id):
    
    # banned_id와 user_id를 전부 탐색하기 위한 조합
    permutation = list(permutations(user_id,len(banned_id)))
    
    # 중복을 막기위한 리스트
    ban_set = []
    
    for user in permutation:
        if not check(user,banned_id):
            continue
        else:
            user = set(user)
            if user not in ban_set:
                ban_set.append(user)
    
    return len(ban_set)
