rows, cols = map(int, input().split())

A = []
B = []
for _ in range(rows):
    A.append(list(map(int, input())))
for _ in range(rows):
    B.append(list(map(int, input())))

def check(A, B):
    if A == B:
        return True
    return False

##################################
if rows < 3 or cols < 3:
    if check(A, B):
        print(0)
    else:
        print(-1)
    exit()    
##################################

x = (rows // 3) + (rows % 3)
y = (cols // 3) + (cols % 3)

cnt = 0

for i in range(x):
    for j in range(y):
        if check(A, B):
            break
        #trans
        for r in range(3):
            for c in range(3):
                if A[i + r][j + c] == 0:
                    A[i + r][j + c] = 1
                else:
                    A[i + r][j + c] = 0
        cnt += 1

if check(A, B):
    print(cnt)
else:
    print(-1)
