def solution(triangle):
    answer = 0
    
    dp = []
    for i, arr in enumerate(triangle): 
        dp.append([])
        if(i == 0):
            dp[i].append(arr[0])
            continue
        #First
        dp[i].append(dp[i - 1][0] + arr[0])
        #middle
        for j in range(1, len(arr) - 1):
            dp[i].append(max(dp[i - 1][j - 1], dp[i - 1][j]) + arr[j])
        #Last
        dp[i].append(dp[i - 1][len(arr) - 2] + arr[len(arr) - 1])
        
    
    answer = max(dp[len(triangle) - 1])

    return answer
