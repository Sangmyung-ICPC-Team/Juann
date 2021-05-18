N, M = map(int, input().split())
dic = {}
for _ in range(N):
    dic[input()] = 1

cnt = 0
for _ in range(M):
    string = input()
    if string in dic.keys():
        cnt += 1
print(cnt)