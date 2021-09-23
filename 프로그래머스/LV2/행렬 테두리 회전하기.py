def solution(rows, columns, queries):
    count = 1 
    answer =[]
    arr = [[0] * columns for _ in range(rows)]
    
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = count
            count += 1

    
    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = arr[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            arr[i-1][query[1]] = arr[i][query[1]]
            small = min(small, arr[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            arr[query[2]][i-1] = arr[query[2]][i]
            small = min(small, arr[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            arr[i+1][query[3]] = arr[i][query[3]]
            small = min(small, arr[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            arr[query[0]][i+1] = arr[query[0]][i]
            small = min(small, arr[query[0]][i])
        arr[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    
    return answer
