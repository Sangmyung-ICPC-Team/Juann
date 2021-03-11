from collections import deque

index = 0
while True:
    index += 1
    string = list(input())
    if '-' in string:
        break
    stack = deque([])

    cnt = 0
    for i in string:
        if i == '{':
            stack.append(i)
        if i == '}':
            #stack is empty
            if not len(stack):
                cnt += 1
                stack.append('{')
                continue
            #stack isn't empty
            op = stack.pop()
    
    if len(stack):
        cnt += (len(stack) // 2) + (len(stack) % 2) 
    print(str(index) + '.', cnt)
    stack.clear()
