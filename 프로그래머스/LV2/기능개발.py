def solution(progresses, speeds):
    answer = []

    time = 0
    count = 0

    while progresses:
        if progresses[0] + (time * speeds[0]) >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)

        else:
            if count > 0:
                answer.append(count)
                count = 0

            time += 1

    # 마지막 작업은 무조건 100 이상으로 끝나므로 else문의 append가 적용되지 않으므로 while문을 탈출하고 나머지를 처리해줌
    answer.append(count)
    return answer