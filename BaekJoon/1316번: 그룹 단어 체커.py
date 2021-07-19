import sys
input = sys.stdin.readline

def is_group(word):
    a_dict = dict()
    temp = word[0]
    for w in word:
        if temp != w and w in a_dict:
            return False
        a_dict[w] = True
        temp = w
    return True

num = int(input())
cnt = 0
for _ in range(num):
    word = input()
    if is_group(word):
        cnt += 1
print(cnt)
