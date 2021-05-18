N = int(input())
loc = list(map(int, input().split()))

#중복 제거
dplc = []
for i in range(N):
    if loc[i] not in dplc:
        dplc.append(loc[i])

dplc.sort() #오름차순 정렬
dic = {} #dictionary 생성

length = len(dplc)
for i in range(length):
    dic[dplc[i]] = i

for i in range(N):
    print("%d" % dic[loc[i]], end=' ')