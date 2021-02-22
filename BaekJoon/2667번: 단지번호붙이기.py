cnt = 0
def depth_first_search(size, square, row, col):
    if row < 0 or row >= size or col < 0 or col >= size:
        return False
    if square[row][col] == 1:
        global cnt #Use cnt for global cnt
        cnt += 1
        square[row][col] = 0
        depth_first_search(size, square, row - 1, col)
        depth_first_search(size, square, row, col - 1)
        depth_first_search(size, square, row + 1, col)
        depth_first_search(size, square, row, col + 1)
        return True
    return False

N = int(input())

#Create table
square = []
for i in range(N):
    square.append(list(map(int, input())))

scope = 0
result = []
for i in range(N):
    for j in range(N):
        if depth_first_search(N, square, i, j) == True:
            scope += 1
            result.append(cnt)
            cnt = 0

print(scope)
result.sort()
for i in result:
    print(i)
