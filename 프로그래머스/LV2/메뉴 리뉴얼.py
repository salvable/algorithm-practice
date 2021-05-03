# combinations , Counter 사용법 숙지할것

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    
    for i in course:
        temp = []
        for order in orders:
            combination = combinations(sorted(order),i)
            temp += combination
        count = Counter(temp)
        
        if len(count) != 0 and max(count.values()) != 1:
            for c in count:
                if count[c] == max(count.values()):
                    answer.append("".join(c))
    return sorted(answer)
