def solution(n, words):
    tmp = ""    
    human = [0] * n 
    wordlist = []
    answer = []
    
    for i in range(len(words)):

        #말한 단어가 아닐경우에 
        if words[i] not in wordlist:
            # 첫번째 단어일 경우
            if i == 0:
                wordlist.append(words[i])
                human[i%n] += 1
                tmp = words[i][-1]
            # 첫번째 단어가 아니고 끝말잇기가 제대로 된 경우
            elif i != 0 and tmp == words[i][0]:
                wordlist.append(words[i])
                human[i%n] += 1
                tmp = words[i][-1]
            # 끝말 잇기가 제대로 되지 않은 경우
            else:
                human[i%n] += 1
                answer.append(i%n+1)
                answer.append(human[i%n])
                break

        # 중복된 단어를 말한 경우        
        else: 
            human[i%n] += 1
            answer.append(i%n+1)
            answer.append(human[i%n])
            break
    else:
        return [0,0]
    
    
    return answer
