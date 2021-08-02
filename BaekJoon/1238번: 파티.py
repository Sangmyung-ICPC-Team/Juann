import sys, heapq
from collections import defaultdict

INF = int(1e9)

def dijkstra(graph, start):
    queue = []
    distances = [INF] * (N + 1)
    heapq.heappush(queue, (0, start))

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        if distances[curr_node] < curr_dist:
            continue

        for node in graph[curr_node]:
            cost = curr_dist + node[1]
            if distances[node[0]] > cost:
                distances[node[0]] = cost
                heapq.heappush(queue, (cost, node[0]))
    return distances

N, M, X = map(int, sys.stdin.readline().split())

graph = defaultdict(list)

for _ in range(M):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

result = dict()
for node in range(1, N + 1):
    result[node] = dijkstra(graph, node)

maximum = -1
for node in range(1, N + 1):
    if node == X:
        continue
    temp = result[node][X] + result[X][node]
    if maximum < temp:
        maximum = temp
print(maximum)
