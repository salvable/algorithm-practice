def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    
    def union(x,y):
        x = find(x)
        y = find(y)
        if x < y:
            parent[y] = x
        else:
            parent[x] = y
    def find(x):
        if parent[x] == x:
            return x
        return find(parent[x])
    
    costs.sort(key = lambda x : x[2])
    price = 0
    count = 0
    for s,e,c in costs:
        if find(s) != find(e):
            union(s,e)
            price += c
            count += 1
            if count == n + 1:
                return price

    return price
