N, M = map(int, input().split())

#input
group = {}
for _ in range(N):
    team = input()
    member = int(input())
    group[team] = []
    for _ in range(member):
        name = input()
        group[team].append(name)
    #사전순 정렬
    group[team].sort()

for _ in range(M):
    name = input()
    cmd = int(input())
    if cmd:
        for value in group.keys(): #key들의 모임에서 
            if name in group[value]: #key에 해당하는 value가 존재하면 
                print(value) #key값 출력
                break
    else:
        for value in group[name]: #key값에 해당하는 value들 모두 출력
            print(value)