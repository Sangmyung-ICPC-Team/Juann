# input
n, m, r = map(int, input().split())
reward = list(map(int, input().split()))
graph = {}
for _ in range(r):
    # u - v, cost
    u, v, c = map(int, input().split())
    
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append([v, c])
    graph[v].append([u, c])

for i in range(1, n + 1):
    if i not in graph:
        graph[i] = []

import heapq
def dijkstra(graph, start):
    
    queue = []
    # node # starts 1 to n
    distances = [float('inf') for _ in range(n+1)]
    distances[start] = 0
    
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        curr_distance, curr_destination = heapq.heappop(queue)
        
        if distances[curr_destination] < curr_distance:
            continue
    
        
        for new_destination, new_distance in graph[curr_destination]:
            distance = curr_distance + new_distance
            
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
                
    return distances


answer = 0
for i in range(n): # 0 ~ n-1
    # i is a start node
    i_distances = dijkstra(graph, i+1) # 1 ~ n
    visited = []
    for idx, d in enumerate(i_distances):
        if idx < 1:
            continue
        if m >= d:
            visited.append(idx)
    
    temp = 0
    for idx in visited:
        temp += reward[idx - 1]
    
    if temp > answer:
        answer = temp

print(answer)
