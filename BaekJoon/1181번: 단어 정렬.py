import sys
N = int(input())

word = []
for _ in range(N):
   temp = sys.stdin.readline()
   if temp not in word:
       word.append(temp)
    
word = sorted(sorted(word), key=len)

for value in word:
    print(value, end='')
