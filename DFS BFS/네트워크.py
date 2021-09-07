def dfs(i,computer,visited):
    if visited[i] == 0:
        visited[i] = 1
    
    for j in range(len(computer)):
        if computer[i][j] == 1 and visited[j] == 0:
            dfs(j,computer,visited)

def solution(n, computers):
    # 방문 리스트
    visited = [0] * n
    answer = 0
    while 0 in visited:
        for i in range(n):
            if visited[i] == 0:
                #dfs로 연결 된 것 다 방문 후 answer + 1
                dfs(i,computers,visited)
                answer += 1
    return answer
