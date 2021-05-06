import sys
sys.setrecursionlimit(10**5)

N, M = map(int, input().split()) #(row, col)
iceberg = [list(map(int, input().split())) for _ in range(N)]

#visited = [[0] * M for _ in range(N)]

def dfs(x, y, iceberg, N, M, visited):
    if x < 0 or x >= N or y < 0 or y >= M:
        return -1
    if visited[x][y] == 0 and iceberg[x][y] > 0:
        visited[x][y] = 1
        cnt = [] #동서남북 바닷물 확인
        cnt.append(dfs(x + 1, y, iceberg, N, M, visited))
        cnt.append(dfs(x - 1, y, iceberg, N, M, visited))
        cnt.append(dfs(x, y + 1, iceberg, N, M, visited))
        cnt.append(dfs(x, y - 1, iceberg, N, M, visited))
        iceberg[x][y] -= cnt.count(0) #0의 개수 만큼
        if iceberg[x][y] < 0:
            iceberg[x][y] = 0
        #check how many 0
        return 1
    if visited[x][y] == 1: #이미 방문한 곳
        return -2
    elif iceberg[x][y] == 0: #iceberg가 0인 곳
        return 0


#all filled with 0
def check_zero(iceberge):
    for loc in iceberg:
        for ice in loc:
            if ice > 0:
                return True
    return False

#main
part = 0
day = 0
#part < 2 or 
while check_zero(iceberg):
    part = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0 and iceberg[i][j] > 0:
                dfs(i, j, iceberg, N, M, visited)
                part += 1
    if part > 1:
        break
    day += 1
    
if part == 1:
    print(0)
else:
    print(day)
