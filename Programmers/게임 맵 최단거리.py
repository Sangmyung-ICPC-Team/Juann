from collections import deque
def solution(graph):
    answer = 0
    
    # Breadth First Search
    
    n, m = len(graph), len(graph[0]) # n과 m은 모두 1 이상이다.
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1] # 동,서,남,북 움직일 방향 설정
    
    queue = deque()
    queue.append((0, 0)) # start 위치
    
    while queue: # queue가 empty일 때까지 iteration
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    if graph[n-1][m-1] == 1: # 최종 dst인 (n, m)에 도달하지 못한 경우
        answer = -1
    else:
        answer = graph[n-1][m-1]
    
    return answer
