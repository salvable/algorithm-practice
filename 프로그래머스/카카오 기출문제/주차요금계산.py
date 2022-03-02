import math


def timeToMinute(time):
    h, m = map(int, time.split(":"))

    return h * 60 + m


def solution(fees, records):
    answer = []

    car = dict()

    for i in range(len(records)):
        # 각각 시간 , 차번호, in,out 기록
        time, car_number, b = records[i].split(" ")
        time = timeToMinute(time)

        if car_number in car.keys():
            car[car_number].append([time, b])
        else:
            car[car_number] = [[time, b]]

    for number in sorted(car.keys()):
        price = 0

        # in이 마지막인 것을 체크할 플래그
        flag = False
        for i in car[number]:
            if i[1] == "IN":
                price -= int(i[0])
                flag = True
            else:
                price += int(i[0])
                flag = False

        # 마지막이 in으로 끝나면
        if flag:
            price += timeToMinute("23:59")

        if price <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((price - fees[0]) / fees[2]) * fees[3])

    return answer