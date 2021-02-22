def depth_first_search(graph, M, N, x, y):
    if x <= -1 or x >= M or y <= -1 or y >= N:
        return False
    if graph[y][x] == 1:
        graph[y][x] = 0 #Check
        depth_first_search(graph, M, N, x - 1, y)
        depth_first_search(graph, M, N, x, y - 1)
        depth_first_search(graph, M, N, x + 1, y)
        depth_first_search(graph, M, N, x, y + 1)
        return True
    return False

T = int(input()) #Test Case

for i in range(T):
    M, N, K = map(int, input().split())
    #Create adj_matrix
    graph = [[0] * M for j in range(N)]
    #Fill in the blank
    for k in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    #Execute
    result = 0
    for a in range(N):
        for b in range(M):
            if depth_first_search(graph, M, N, b, a) == True:
                result += 1
    print(result)
