from collections import deque
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

def get_loc_shark():
    for i, row in enumerate(graph):
        if 9 in row:
            return i, row.index(9)

s_row, s_col = get_loc_shark() #where is shark?

queue = deque()
queue.append((s_row, s_col)) #start location

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N: #in the field
                