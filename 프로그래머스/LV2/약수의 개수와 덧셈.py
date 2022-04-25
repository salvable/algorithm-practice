def solution(left, right):
    answer = 0
    # 1,2 해결해야..
    for i in range(left, right + 1):

        temp = []

        for j in range(1, i + 1):
            if i % j == 0:
                if j not in temp:
                    temp.append(j)
                if i // j not in temp:
                    temp.append(i // j)

        if len(temp) % 2 == 0:
            answer += i

        else:
            answer -= i

    return answer