#(1)
M, N, K = map(int, input().split()) #rows, cols : y, x
field = [[0] * N for _ in range(M)] #cols, rows

#(2) error
for i in range(K):
    #left_bottom: lb / right_top: rt
    lb_x, lb_y, rt_x, rt_y = map(int, input().split())
    for i in range(M - rt_y, M - lb_y):
        for j in range(lb_x, rt_x):
            if field[i][j] == 0:
                #create wall
                field[i][j] = 1
#->field reverse

breath = 0 
# /*depth first search*/ #
def depth_first_search(x, y):
    global breath
    if x >= M or x < 0 or y >= N or y < 0:
        return False
    if field[x][y] == 0:
        breath += 1
        field[x][y] = 1 
        depth_first_search(x + 1, y)
        depth_first_search(x - 1, y)
        depth_first_search(x, y + 1)
        depth_first_search(x, y - 1)
        return True
    return False

#(3)
cnt = 0
result = []
for i in range(M):
    for j in range(N):
        if depth_first_search(i, j):
            result.append(breath)
            cnt += 1
            breath = 0

print(cnt)
result.sort()
for value in result:
    print(value, end=' ')