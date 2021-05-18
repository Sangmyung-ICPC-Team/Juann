def depth_first_search(adj_matrix, visited, vertex):
    visited[vertex] = True
    for i in range(len(adj_matrix[vertex])):
        if adj_matrix[vertex][i] == 1 and visited[i] == False:
            depth_first_search(adj_matrix, visited, i)

def print_result(case, cnt):
    if cnt > 1:
        print('Case ', case, ': ', 'A forest of ', cnt, ' trees.')
    elif cnt == 1:
        print('Case ', case, ': ', 'There is one tree.')
    else:
        print('Case ', case, ': ', 'No trees.')

case = 0
while True:
    case += 1
    n, m = map(int, input().split()) #number of vertex and edge
    if n == 0 and m == 0:
        break
    adj_matrix = [[0] * n for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj_matrix[u][v] = 1
        adj_matrix[v][u] = 1
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if visited[i] == False:
            depth_first_search(adj_matrix, visited, i)
            cnt += 1
    print_result(case, cnt)



