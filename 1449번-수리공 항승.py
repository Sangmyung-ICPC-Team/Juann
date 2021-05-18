N, L = map(int, input().split())

pipe = list(map(int, input().split()))
pipe.sort() #입력 데이터가 무작위로 주어지기 때문

cnt = 0
tmp = 0

for p in pipe:
    if tmp < p:
        cnt += 1
        tmp = p + L - 1

print(cnt)

'''
L -= 0.5
flag = False
cnt = 0
for i in range(N - 1):
    if flag:
        flag = False
        continue
    pipe[i] += L
    cnt += 1
    if pipe[i] >= pipe[i + 1] + 0.5:
        flag = True

if flag == False:
    cnt += 1

print(cnt)
'''