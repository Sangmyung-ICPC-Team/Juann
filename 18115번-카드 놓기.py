from collections import deque

N = int(input())
cmd = list(map(int, input().split()))
cmd.reverse()

d = deque([])
for i, value in zip(cmd, range(1, N + 1)):
    if i == 1:
        d.append(value)
    elif i == 2:
        temp = d.pop()
        d.append(value)
        d.append(temp)
    elif i == 3:
        d.appendleft(value)

d.reverse()
for i in d:
    print(i, end=' ')
