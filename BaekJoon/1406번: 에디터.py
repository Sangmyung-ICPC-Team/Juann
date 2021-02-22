stk1 = list(input())
M = int(input())

stk2 = []

for i in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        if stk1:
            stk2.append(stk1.pop()) #stk1 -> stk2
    elif cmd[0] == 'D':
        if stk2:
            stk1.append(stk2.pop()) #stk2 -> stk1
    elif cmd[0] == 'B':
        if stk1:
            stk1.pop()
    elif cmd[0] == 'P':
        stk1.append(cmd[1])

stk2.reverse()
for i in stk1:
    print(i, end='')
for i in stk2:
    print(i, end='')

