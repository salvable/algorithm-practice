#시간을 모두 초로 바꾸는 함수
def time_to_int(time):
    h, m , s = time.split(":")
    
    return int(h) * 3600 + int(m) * 60 + int(s)

#초단위의 숫자를 시간으로 바꾸는 함수
def int_to_time(time):
    h = str(time // 3600)
    # h가 10보다 작을경우 앞에 0을 추가시켜줘야 함
    if int(h) < 10:
        h = "0" + h
    
    time = time % 3600
    m = str(time // 60)
    if int(m) < 10:
        m = "0" + m
        
    s = str(time % 60)
    if int(s) < 10:
        s = "0" + s
    
    return h + ":" + m + ":" + s
    

def solution(play_time, adv_time, logs):
    play_time = time_to_int(play_time)
    adv_time = time_to_int(adv_time)
    
    #플레이타임의 초 길이만큼 배열을 만들어줌
    total_time = [0 for _ in range(play_time + 1)]

    for log in logs:
        start, end = log.split("-")
        start = time_to_int(start)
        end = time_to_int(end)
        
        # 시작지점에는 시청을 시작했으니 +1 을 해주고 end지점에는 -1을 기록
        total_time[start] += 1
        total_time[end] -= 1
    
    # 리스트에 구간별 시청자수를 기록
    for i in range(1,len(total_time)):
        total_time[i] = total_time[i] + total_time[i-1]
    
    # 같은 방식으로 리스트 전체의 누적 시청자 수를 기록
    for i in range(1,len(total_time)):
        total_time[i] = total_time[i] + total_time[i-1]
        
    most = 0
    max_time = 0
    
    # 전체를 탐색하며 최고 시청자수를 가지는 시간 기록
    for i in range(adv_time - 1 , play_time):
        if i >= adv_time:
            if most < total_time[i] -  total_time[i - adv_time]:
                most = total_time[i] -  total_time[i - adv_time]
                max_time = i - adv_time + 1
        # 0초부터 광고가 시작하는 경우 예외처리
        else:
            if most < total_time[i]:
                most = total_time[i]
                max_time = i - adv_time + 1
                
    return int_to_time(max_time)
