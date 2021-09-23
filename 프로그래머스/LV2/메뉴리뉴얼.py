from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    
    for i in course:
        combination = []
        for order in orders:
            combination += combinations(sorted(order), i)
        
        count = Counter(combination)
        
        if len(count) != 0 and max(count.values()) > 1:
            for c in count:
                if count[c] == max(count.values()):
                    answer.append("".join(c))
    
    return sorted(answer)
