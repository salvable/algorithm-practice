from collections import deque

def solution(cacheSize, cities):
    
    cache = deque()
    cities = [i.lower() for i in cities]
    time = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    else:
        for i in cities:
            # cache안에 해당 도시가 있을경우 LRU 캐시교체알고리즘을 이용해야하므로 remove 이후 append로 제일 뒤로 붙여줌
            if i in cache:
                time += 1
                cache.remove(i)
                cache.append(i)
            else:
                time += 5
                
                # 사이즈보다 작으면 가장 오래된 항목을 빼고 넣어주고 사이즈보다 작으면 그냥 넣어줌
                if len(cache) >= cacheSize:
                    cache.popleft()
                    cache.append(i)
                else:
                    cache.append(i)
                    
    return time
