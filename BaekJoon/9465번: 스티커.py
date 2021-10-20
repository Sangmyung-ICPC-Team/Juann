testCase = int(input())

def maxProfit(row, stk):
    dp = [[0 for _ in range(row+1)] for _ in range(2)]
    dp[0][1], dp[1][1] = stk[0][0], stk[1][0]

    for idx in range(2, row + 1):
        dp[0][idx] = max(max(dp[0][idx-2], dp[1][idx-2]), dp[1][idx-1]) + stk[0][idx-1]
        dp[1][idx] = max(max(dp[0][idx-2], dp[1][idx-2]), dp[0][idx-1]) + stk[1][idx-1]

    return max(dp[0][row], dp[1][row])

for _ in range(testCase):
    row = int(input())
    sticker = [list(map(int,input().split())) for _ in range(2)]
    print(maxProfit(row, sticker))
