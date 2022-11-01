# setting
from collections import deque
import sys
f = sys.stdin.readline

# input init
n, m, k, x = map(int, f().split())
graph = dict.fromkeys([i for i in range(n+1)], []) #[[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

# input edges
for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

   
def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
                
                if distance[i] == k:
                    answer.append(i)
    # False
    if len(answer) == 0:
        print(-1)
    # True
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(x)
