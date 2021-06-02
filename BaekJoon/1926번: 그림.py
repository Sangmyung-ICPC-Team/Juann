import sys
sys.setrecursionlimit(10**6)

def bfs(paper, rows, cols, x, y):
    cnt = 0
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return 0
    if paper[x][y] == 1:
        cnt += 1
        paper[x][y] = 0
        cnt += bfs(paper, rows, cols, x + 1, y)
        cnt += bfs(paper, rows, cols, x - 1, y)
        cnt += bfs(paper, rows, cols, x, y + 1)
        cnt += bfs(paper, rows, cols, x, y - 1)
        return cnt
    return 0


rows, cols = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(rows)]

cnt = 0
biggest = 0
for i in range(rows):
    for j in range(cols):
        picture = bfs(paper, rows, cols, i, j)
        if picture > 0:
            cnt += 1
            if picture > biggest:
                biggest = picture
print(cnt, biggest, sep='\n')
