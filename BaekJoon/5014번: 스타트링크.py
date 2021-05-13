from collections import deque

F, S, G, U, D = map(int, input().split())
#F는 전체 건물의 층 수, G는 스타트링크의 위치, S는 현재 위치 
def breath_first_search(F, S, G, U, D):
    #bfs를 위해 필요한 것들 
    visited = set() #deque()
    queue = deque()
    
    queue.append((0, S))
    visited.add(S)
    
    while queue:
        cnt, stairs = queue.popleft()
        if stairs == G: #해당 층(G)에 도착한 경우
            return cnt
        #위로 U만큼 갔을 때 F(최대 높이)보다 작거나 같다 & 방문하지 않은 곳인 경우
        if stairs + U <= F and stairs + U not in visited:
            visited.add(stairs+U)
            queue.append((cnt + 1, stairs + U))
        #아래로 D만큼 내려갔을 때 1보다 크거나 같다 & 방문하지 않은 곳인 경우
        if stairs - D >= 1 and stairs - D not in visited:
                visited.add(stairs - D)
                queue.append((cnt + 1, stairs - D))
    #도달하지 못 할 경우
    return "use the stairs"

print(breath_first_search(F, S, G, U, D))
