def solution(id_list, report, k):
    dic = dict()
    answer = dict()

    for id in id_list:
        if id not in dic.keys():
            dic[id] = []
            answer[id] = 0

    for r in report:
        user_id, report_id = r.split(" ")

        if user_id not in dic[report_id]:
            dic[report_id].append(user_id)

    for report_id, user_arr in dic.items():
        if len(user_arr) >= k:
            for i in user_arr:
                answer[i] += 1

    return list(answer.values())