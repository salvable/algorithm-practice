def solution(genres, plays):
    
    answer = []
    
    # 총 재생횟수 dictionary
    total_dic = dict()
    # [(장르,횟수)] dictionary
    dic = dict()
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        if genre in total_dic.keys():
            total_dic[genre] += play
            dic[genre].append((play,i))
        else:
            total_dic[genre] = play
            dic[genre] = [(play,i)]
    
    total = sorted(total_dic.items(), key = lambda x: x[1], reverse=True)
    
    for i in dic:
        dic[i] = sorted(dic[i], key = lambda x: -x[0])[:2]
    
    for i in total:
        for j in dic[i[0]]:
            answer.append(j[1])
    
    return answer
