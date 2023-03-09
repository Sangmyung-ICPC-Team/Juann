# number of cities, edges, power stations 
N, M, K = map(int, input().split())

# nodes of power station
power_stations = list(map(int, input().split()))


import heapq, sys
# sys.setrecursionlimit(10**8)

graph = {}

for i in range(M):
    u, v, w = map(int, input().split())
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
        
    graph[u].append([w, u, v])
    graph[v].append([w, v, u])
    
    


def prim(graph, start, visited):
    temp = []
    for i in power_stations:
        visited[i] = 1
        temp += graph[i]
    
    
    heapq.heapify(temp)
    mst = []
    
    total_weight = 0
    
    while temp:
        w, u, v = heapq.heappop(temp)
        
        if visited[v] == 0:
            visited[v] = 1
            if u < v:
                mst.append([u, v])
            else:
                mst.append([v, u])
            total_weight += w
            
            for e in graph[v]:
                if visited[e[2]] == 0:
                    heapq.heappush(temp, e)
           #        
    return total_weight


visited = [0] * (N + 1)

print(prim(graph, i, visited))
