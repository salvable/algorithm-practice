def solution(info, edges):
    def dfs(sheep, wolf, node, arr):
        if info[node]:
            wolf += 1
        else:
            sheep += 1

        # 늑대가 양보다 많아지는 루트는 무시
        if wolf >= sheep:
            return 0

        maxSheep = sheep

        for a in arr:
            for n in graph[a]:
                # 백트래킹으로 현재 루트에 n이 없을경우 진행하여 줌
                if n not in arr:
                    arr.append(n)
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n, arr))
                    arr.pop()

        return maxSheep

    graph = [[] for _ in range(len(info))]

    for i in range(len(edges)):
        a, b = edges[i]
        graph[a].append(b)

    # 양 갯수, 늑대 갯수, 현재 노드, 현재 포함하고 있는 루트
    answer = dfs(0, 0, 0, [0])
    return answer