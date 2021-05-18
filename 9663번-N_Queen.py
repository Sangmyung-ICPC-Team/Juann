cnt = 0 #경우의 수

def promising(i, col):
    k = 1
    flag = True
    while(k < i and flag):
        #가로,세로 판별 or 대각선 판별 
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            return False
        k += 1
    return flag

def n_queen(i, col):
    global cnt
    n = len(col) - 1
    if promising(i, col):
        if i == n:
            cnt += 1
            return
            #print(col[1:n+1])
        else:
            for j in range(1, n+1):
                col[i + 1] = j
                n_queen(i+1, col)

n = int(input())
#col의 row 번호 
col = [0] * (n+1)
n_queen(0, col)
print(cnt)