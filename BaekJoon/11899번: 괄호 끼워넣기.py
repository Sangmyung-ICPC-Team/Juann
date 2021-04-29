string = input()
length = len(string)

stack = []
cnt = 0
for i in range(length - 1, -1, -1):
    if string[i] == ')':
        stack.append(string[i])
    else:
        if len(stack) == 0:
            cnt += 1
            continue
        stack.pop()

cnt += len(stack)
print(cnt)

