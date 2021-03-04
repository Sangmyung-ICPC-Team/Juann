def depth_first_search(island, w, h, x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False
    if island[x][y] == '1':
        island[x][y] = '0'
        #상하좌우
        depth_first_search(island, w, h, x + 1, y)
        depth_first_search(island, w, h, x - 1, y)
        depth_first_search(island, w, h, x, y + 1)
        depth_first_search(island, w, h, x, y - 1)
        #대각선
        depth_first_search(island, w, h, x + 1, y - 1)
        depth_first_search(island, w, h, x - 1, y + 1)
        depth_first_search(island, w, h, x + 1, y + 1)
        depth_first_search(island, w, h, x - 1, y - 1)
        return True
    return False

        
while True:
    island = []
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    for i in range(h):
        island.append(input().split())
    cnt = 0
    for i in range(h):
        for j in range(w):
            if depth_first_search(island, w, h, i, j) == True:
                cnt += 1
    print(cnt)
