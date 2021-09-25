from itertools import permutations
def solution(numbers):
    number_list = list(numbers)
    length = len(number_list)
    
    combination = []
    
    for i in range(1,length + 1):
        combination += list(permutations(number_list,i))

    number = set()
    
    for c in combination:
        digit = int("".join(c))
        number.add(digit)
    
    result = []
    
    for i in number:
        if i < 2:
            continue
        
        check = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                check = False
                break
                
        if check:
            result.append(i)
    
    return len(result)
