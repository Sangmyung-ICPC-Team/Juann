rows, cols = map(int, input().split())
graph = [list(input()) for _ in range(rows)]

from collections import deque

def normalize(g, rows, cols):   
    for i in range(rows):
        for j in range(cols):
            if g[i][j] == 'L':
                g[i][j] = 0
            '''
            else:
                g[i][j] = 1
            '''

def bfs(g, rows, cols, x, y):
    m = -1
    queue = deque()
    queue.append((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                continue
            if g[nx][ny] == 0 and visited[nx][ny] == False:        
                g[nx][ny] = g[x][y] + 1
                if g[nx][ny] > m:
                    m = g[nx][ny]
                queue.append((nx, ny))
    return m

import copy

result = -1 
normalize(graph, rows, cols)
for i in range(rows):
    for j in range(cols):
        if graph[i][j] == 0:
            temp = copy.deepcopy(graph)
            x = bfs(temp, rows, cols, i, j)
            if result < x:
                result = x
print(result)
