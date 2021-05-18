import copy
import sys
#recursion depth 임의로 증가 < 10 ^ 5
sys.setrecursionlimit(10**5)

def depth_first_search(color, x, y, num, before):
    if x < 0 or x >= num or y < 0 or y >= num:
        return False
    if color[x][y] != 'X' and color[x][y] == before:
        value = color[x][y]
        color[x][y] = 'X'
        depth_first_search(color, x + 1, y, num, value)
        depth_first_search(color, x - 1, y, num, value)
        depth_first_search(color, x, y + 1, num, value)
        depth_first_search(color, x, y - 1, num, value)
        return True
    return False

num = int(input())
color = [] #R, G, B

for i in range(num):
    color.append(list(input()))

temp = copy.deepcopy(color) #deep copy

cnt = 0
for i in range(num):
    for j in range(num):
        if depth_first_search(color, i, j, num, color[i][j]) == True:
            cnt += 1

for i in range(num):
    for j in range(num):
        if temp[i][j] == 'G':
            temp[i][j] = 'R'

count = 0
for i in range(num):
    for j in range(num):
        if depth_first_search(temp, i, j, num, temp[i][j]) == True:
            count += 1
print(cnt, count)
