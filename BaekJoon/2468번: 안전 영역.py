import copy
import sys
sys.setrecursionlimit(10**5)

#input
N = int(input())
arr = [[int(x) for x in input().split()] for y in range(N)]

def depth_first_search(tmp, x, y, height):
    if x >= N or x < 0 or y >= N or y < 0:
        return False
    if tmp[x][y] > height:
        tmp[x][y] = -1 #change to always flooded
        depth_first_search(tmp, x + 1, y, height)
        depth_first_search(tmp, x, y + 1, height)
        depth_first_search(tmp, x - 1, y, height)
        depth_first_search(tmp, x, y - 1, height) 
        return True
    return False


maximum = -1
for i in range(101): # height range : (1 ~ 100)
    cnt = 0 #count of domain
    tmp = copy.deepcopy(arr) #deep copy
    for j in range(N): #x
        for k in range(N): #y
            if depth_first_search(tmp, j, k, i) == True:
                cnt += 1
    if maximum < cnt:
        maximum = cnt

print(maximum)
