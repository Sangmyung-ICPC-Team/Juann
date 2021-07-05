n = int(input()) #vertex
S,D = map(int, input().split()) #start, destination
m = int(input()) #edge

edges = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    edges[u - 1][v - 1] = 1
    edges[v - 1][u - 1] = 1

visited = [False for _ in range(n)]
cnt = 0
def dfs(edges, s, d, cnt):
    visited[s] = True #check
    if s == d: #is destination?
        print(cnt)
        exit()
    cnt += 1
    for i in range(len(edges[s])):
        if edges[s][i] == 1 and visited[i] == False:
            dfs(edges, i, d, cnt)
    
dfs(edges, S - 1, D - 1, cnt)
print(-1)
