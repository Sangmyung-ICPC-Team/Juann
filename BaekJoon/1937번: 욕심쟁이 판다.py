import sys
sys.setrecursionlimit(10**6)

def depth_first_search(x, y):
    if dp[x][y]:
        return dp[x][y]
    dp[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] > board[x][y]:
                dp[x][y] = max(dp[x][y], depth_first_search(nx, ny) + 1)
    return dp[x][y]


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

answer = 1
for i in range(n):
    for j in range(n):
        answer = max(answer, depth_first_search(i, j))
        print(answer)
print(answer)
