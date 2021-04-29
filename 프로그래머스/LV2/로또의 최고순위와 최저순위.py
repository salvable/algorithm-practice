def solution(lottos, win_nums):
    lottos.sort(reverse = True)
    # 맞은 로또
    lotto_count = 0
    # 지워진 갯수
    zero_count = 0
    
    #순위를 담은 리스트
    rank = [6,6,5,4,3,2,1]
    answer = []
    
    for i in lottos:
        if i != 0 and i in win_nums:
            lotto_count += 1
        if i == 0:
            zero_count += 1

    return [rank[lotto_count+zero_count] , rank[lotto_count]]
