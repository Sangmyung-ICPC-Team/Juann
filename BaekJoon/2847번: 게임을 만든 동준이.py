# Greedy approach #

num = int(input())
level_score = []

for _ in range(num):
    n = int(input())
    level_score.append(n)

level_score.reverse() #descending order by level

cnt = 0
for i in range(num - 1):
    while level_score[i] <= level_score[i + 1]:
        level_score[i + 1] -= 1
        cnt += 1

print(cnt)

