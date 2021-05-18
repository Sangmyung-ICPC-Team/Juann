N, M = map(int, input().split())

vertex = [[0] * (N + 1) for i in range(N + 1)]
visited = [False] * (N + 1)

#input
for _ in range(M):
    u, v = map(int, input().split())
    vertex[u][v] = 1
    vertex[v][u] = 1

cnt = 0
def depth_first_search(v, visited):
    visited[v] = True
    for i in range(1, (N + 1)):
        if visited[i] == False and vertex[v][i] == 1:
            depth_first_search(i, visited)
for i in range(1, (N + 1)):
    if visited[i] == False:
        depth_first_search(i, visited)
        cnt += 1
print(cnt)