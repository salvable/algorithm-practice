# 중복 조합이용
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [0 for i in range(11)]
    max_diff = 0

    result = False
    for r in list(combinations_with_replacement(range(0, 11), n)):
        score = [0 for i in range(11)]

        for i in r:
            score[10 - i] += 1

        lion = 0
        peach = 0

        # 각각은 인덱스, 라이언, 어피치
        for i, (l, p) in enumerate(zip(score, info)):
            # 둘다 0발인경우
            if l == p == 0:
                continue
            # 어피치가 많이 쏘거나 같은경우
            if l <= p:
                peach += 10 - i
            elif l > p:
                lion += 10 - i

        if lion > peach:
            result = True
            if lion - peach > max_diff:
                max_diff = lion - peach
                answer = score

    if not result:
        return [-1]

    return answer