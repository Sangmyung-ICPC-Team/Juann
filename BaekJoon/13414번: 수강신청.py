import sys
K, L = map(int, sys.stdin.readline().split()) #input

waiting = dict() #create dictionary
for i in range(L):
    no = sys.stdin.readline().strip()
    waiting[no] = i

sorted_order = sorted(waiting.items(), key=lambda x:x[1])
cnt = 0 #최대 수강 인원만큼 출력
for key in sorted_order:
    if cnt == K:
        break
    print(key[0])
    cnt += 1
