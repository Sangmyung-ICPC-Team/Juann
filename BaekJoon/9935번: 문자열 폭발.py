string = input()
bomb = list(input())

stack = []

#length
string_len = len(string)
bomb_len = len(bomb)

#main
for word in string:
    stack.append(word)
    if len(stack) >= bomb_len:
        x = len(stack) - bomb_len
        if stack[x:] == bomb:
            for _ in range(bomb_len):
                stack.pop()
        

if len(stack):
    for value in stack:
        print(value, end='')
else:
    print("FRULA")
