def dfs(n, computers, vertex, visited):
    visited[vertex] = True
    for i in range(n):
        if computers[vertex][i] == 1 and visited[i] == False:
            dfs(n, computers, i, visited)

def solution(n, computers):
    visited = [False] * n

    #depth first search
    cnt = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and visited[j] == False:
                dfs(n, computers, j, visited)
                cnt += 1
            
    answer = cnt
    return answer
