def solution(cacheSize, cities):
    
    cache = []
    cities = [city.lower() for city in cities]
    time = 0
    
    if(cacheSize != 0):
        for city in cities:
            #캐시안에 해당 도시가 있는경우
            if city in cache:
                cache.pop(cache.index(city))
                cache.append(city)
                time += 1
            else:
                #해당 도시가 캐시안에 없고 cache가 가득차지 않은 경우
                if len(cache) < cacheSize:
                    cache.append(city)
                    time += 5
                #제일 오래된 0번째 인덱스를 제거해야 함
                else:   
                    cache.pop(0)
                    cache.append(city)
                    time += 5
    
    #cacheSize가 0 일경우 도시 크기만큼 5 를 곱함
    else: 
        time += len(cities) * 5
    return time
