import sys
from collections import deque
input = sys.stdin.readline

'''
(x-2, y+1) / (x-1, y+2) / (x+2, y+1) / (x+1, y+2)
(x-2, y-1) / (x-1, y-2) / (x+2, y-1) / (x+1, y-2)
'''

def breath_first_search(length, curr_x, curr_y, goal_x, goal_y):
    field = [[0 for _ in range(length)] for _ in range(length)]
    visited = [[False for _ in range(length)] for _ in range(length)]

    queue = deque()
    visited[curr_x][curr_y] = True
    queue.append((curr_x, curr_y))

    dx = [-2, -1, 2, 1, -2, -1, 2, 1]
    dy = [1, 2, 1, 2, -1, -2, -1, -2]

    while queue:
        x, y = queue.popleft()
        if x == goal_x and y == goal_y:
            return field[x][y]
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue
            if visited[nx][ny] == False:
                field[nx][ny] = field[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return 0


if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        l = int(input())
        curr_x, curr_y = map(int, input().split())
        goal_x, goal_y = map(int, input().split())
        if curr_x == goal_x and curr_y == goal_y:
            print(0)
            continue
        print(breath_first_search(l, curr_x, curr_y, goal_x, goal_y))
