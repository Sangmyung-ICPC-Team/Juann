import sys
from collections import deque
input = sys.stdin.readline

def check_ripen(graph, row, col, height, visited, queue):
    for i in range(height):
        for j in range(row):
            for k in range(col):
                if graph[i][j][k] == -1:
                    visited[i][j][k] = True
                elif graph[i][j][k] == 1:
                    queue.append((i, j, k))
                    visited[i][j][k] = True


def breath_first_search(graph, row, col, height, visited):
    queue = deque()
    check_ripen(graph, row, col, height, visited, queue)

    dx = [0, 0, 1, -1, 0, 0]
    dy = [0, 0, 0, 0, -1, 1]
    dz = [1, -1, 0, 0, 0, 0]

    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz, nx, ny = z+dz[i], x+dx[i], y+dy[i]
            #boundary condition
            if (nx < 0 or nx >= row) or (ny < 0 or ny >= col) or (nz < 0 or nz >= height):
                continue
            if visited[nz][nx][ny] == False and graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                visited[nz][nx][ny] = True
                queue.append((nz, nx, ny))

def is_finish(graph, row, col, height):
    m = 0
    for i in range(height):
        for j in range(row):
            for k in range(col):
                if graph[i][j][k] == 0:
                    return -1
                if m < graph[i][j][k]:
                    m = graph[i][j][k]
    return m - 1


if __name__ == "__main__":
    col, row, height = map(int, input().split())
    #Create 3-dimension list
    graph = list()
    for i in range(height):
        temp = [list(map(int, input().split())) for _ in range(row)]
        graph.append(temp)
    visited = [[[False for _ in range(col)] for _ in range(row)] for _ in range(height)]
    if is_finish(graph, row, col, height) == 1:
        print(0)
        exit()
    breath_first_search(graph, row, col, height, visited)
    print(is_finish(graph, row, col, height))
