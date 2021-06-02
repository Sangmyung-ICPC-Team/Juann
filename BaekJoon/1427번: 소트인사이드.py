number = input()

arr = []
for word in number:
    arr.append(int(word))
arr.sort(reverse=True)
for word in arr:
    print(word, end='')
