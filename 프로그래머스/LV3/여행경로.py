from collections import defaultdict
2
​
3
def dfs(s):
4
    global graph, answer
5
    
6
    # graph에 해당 키의 dictionary가 있으면 0번째 인덱스부터 제거해줌
7
    while graph[s]:
8
        dfs(graph[s].pop(0))
9
    
10
    # graph에 해당 키에 없을경우 answer 리스트에 마지막 도착지부터 역으로 쌓임
11
    if not graph[s]:
12
        answer.append(s)
13
        return
14
​
15
def solution(tickets):
16
    global graph, answer
17
    graph = defaultdict(list)
18
    answer = []
19
    
20
    # 출발지를 키값으로 가지는 dictionary에 추가 
21
    for a,b in tickets:
22
        graph[a].append(b)
23
    
24
    # 알파벳순서가 앞서는 경로로 정렬
25
    for a, b in graph.items():
26
        graph[a].sort()
27
        
28
    # ICN 지점부터 출발
29
    dfs("ICN")
30
​
31
​
32
    return answer[::-1]
