from collections import deque
def where_is(field, R, C, queue_w, queue_h):
    for i in range(R):
        for j in range(C):
            if field[i][j] == '*':
                queue_w.append((i, j))
            elif field[i][j] == 'S':
                queue_h.append((i, j))

    
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def game_start(field, R, C, queue_w, queue_h, visited):
    flag = False #is it finish?
    cnt = 1
    while True:
        #First,,water spread
        for i in range(len(queue_w)):
            wx, wy = queue_w.popleft()
            visited[wx][wy] = True
            for i in range(4):
                nx = wx + dx[i]
                ny = wy + dy[i]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                if visited[nx][ny] == False and field[nx][ny] == '.':
                    field[nx][ny] = '*'
                    visited[nx][ny] = True
                    queue_w.append((nx, ny))
        #Second,,hedgehog move
        for i in range(len(queue_h)):
            hx, hy = queue_h.popleft()
            visited[hx][hy] = True
            for i in range(4):
                nx = hx + dx[i]
                ny = hy + dy[i]
                if nx < 0 or nx >= R or ny < 0 or ny >= C:
                    continue
                if field[nx][ny] == 'D':
                    flag = True
                    break
                if visited[nx][ny] == False and field[nx][ny] == '.':
                    field[nx][ny] = 'S'
                    visited[nx][ny] = True
                    queue_h.append((nx, ny))
        if flag:
            return cnt
        if len(queue_w) == 0 and len(queue_h) == 0:
            return 0
        cnt += 1

R, C = map(int, input().split())

#string to list
field = [list(input()) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

queue_w = deque()
queue_h = deque()
where_is(field, R, C, queue_w, queue_h)

result = game_start(field, R, C, queue_w, queue_h, visited)
if result > 0:
    print(result)
else:
    print("KAKTUS")
