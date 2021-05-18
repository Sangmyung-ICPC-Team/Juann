a, b = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dic = {}
for i in A:
    #add
    dic[i] = 1

for i in B:
    #already exist
    if i in dic.keys():
        dic[i] += 1
    #add
    else:
        dic[i] = 1

cnt = 0
for i in dic.keys():
    if dic[i] == 1:
        cnt += 1

print(cnt)


