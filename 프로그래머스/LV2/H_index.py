def solution(citations): 
    
    citations.sort()
    H_index = len(citations)
    
    for i in range(H_index):
        if citations[i] >= H_index-i:
            return H_index-i
        
    return 0
