from collections import deque

#setting
cols, rows = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(rows)]
visited = [[False for _ in range(cols)] for _ in range(rows)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
#check early garden
for i in range(rows):
    for j in range(cols):
        if graph[i][j] == 1: #check tomato
            queue.append((i, j))

#breath first search
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1 #전 날에 하루 추가 
                queue.append((nx, ny))

m = 0 #maximum day
#check number of tomato
def check_garden():
    global m
    for value in graph:
        m = max(max(value), m)
        if 0 in value:
            return False
    return True

#how many days?

#main
bfs() #call func.
if check_garden():
    print(m - 1)
else:
    print(-1)
    
