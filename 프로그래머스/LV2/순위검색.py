from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = dict()

    for i in range(len(info)):
        splitList = info[i].split(" ")
        menu = splitList[:-1]
        score = splitList[-1]
        
        for j in range(5):
            combi = list(combinations(menu,j))
            for c in combi:
                key = "".join(c)
                if key in dic.keys():
                    dic[key].append(int(score))
                else:
                    dic[key] = [int(score)]
    
    for d in dic:
        dic[d].sort()
    
    for q in query:
        splitList = q.split(" ")
        menu = splitList[:-1]
        score = splitList[-1]
        
        while 'and' in menu:
            menu.remove('and')
    
        while '-' in menu:
            menu.remove('-')
        
        key = "".join(menu)
        
        if key in dic.keys():
            scores = dic[key]
            
            if scores:
                index = bisect_left(scores,int(score))
                answer.append(len(scores) - index)
        else:
            answer.append(0)
                
    return answer
