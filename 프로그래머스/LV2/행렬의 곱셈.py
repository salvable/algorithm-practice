def solution(arr1, arr2):
    answer = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1)) ]
 
    for i in range(len(arr1)):
        # 배열 속 원소의 갯수를 통해 접근
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                print(i,j,k)
                answer[i][j] += (arr1[i][k] * arr2[k][j])

    return answer
