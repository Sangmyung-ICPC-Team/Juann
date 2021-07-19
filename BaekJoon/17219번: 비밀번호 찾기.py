import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pw = dict()
for _ in range(N):
    site, string = map(str, input().split())
    site, string= site.strip(), string.strip()
    pw[site] = string

for _ in range(M):
    site = input().strip()
    print(pw[site])
