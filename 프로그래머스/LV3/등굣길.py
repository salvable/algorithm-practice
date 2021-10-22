def solution(m, n, puddles):
    puddles = [[q,p] for [p,q] in puddles]      
    dp = [[0] * (m + 1) for i in range(n + 1)]
    dp[1][1] = 1         

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: 
                continue 
            # 웅덩이일 경우 값을 0 으로 바꿔 다음 계산에서 영향을 받지 않도록 만들어줌
            if [i, j] in puddles:   
                dp[i][j] = 0
            else:                    
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    
    return dp[n][m]
            
