# 문자의 길이에 따라 저장할 리스트 
array = [[] for _ in range(10001)]
reverse_array = [[] for _ in range(10001)]

from bisect import bisect_right, bisect_left

def count_by_range(array, left, right):
    r_index = bisect_right(array,right)
    l_index = bisect_left(array,left)
    
    return r_index - l_index

def solution(words, queries):
    answer = []
    
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])
    
    for i in range(10001):
        array[i].sort()
        reverse_array[i].sort()
    
    for q in queries:
        # 접두사로 ? 를 가질 경우
        if q[0] == "?":
            res = count_by_range(reverse_array[len(q)], q[::-1].replace("?","a"), q[::-1].replace("?","z"))
        else:
            res = count_by_range(array[len(q)],q.replace("?","a"),q.replace("?","z"))
    
        answer.append(res)
    return answer
