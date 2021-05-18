string = input()
target = input()

#length
s_n = len(string)
t_n = len(target)

cnt = 0
i = 0 #index
while i + t_n <= s_n:
    if string[i:i+t_n] == target:
        cnt += 1
        i += t_n
        continue
    i += 1

print(cnt)