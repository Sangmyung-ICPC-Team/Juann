scv = int(input())
hp = list(map(int, input().split()))

damage = [9, 3, 1]
cnt = 0

while len(hp):
    hp.sort(reverse=True) #내림차순 정렬
    for i in range(len(hp)):
        print(hp[i], damage[i])
        hp[i] -= damage[i]
        if hp[i] <= 0:
            
    cnt += 1

print(cnt)
