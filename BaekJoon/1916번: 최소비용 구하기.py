import heapq
import sys

def dijkstra(graph, start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0 #시작 위치는 항상 0

    queue = []
    heapq.heappush(queue, [distances[start], start])
    
    while queue:
        curr_distance, curr_destination = heapq.heappop(queue)

        if distances[curr_destination] < curr_distance:
            continue

        for new_destination, new_distance in graph[curr_destination].items():
            distance = curr_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    return distances

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())

    graph = {node: {} for node in range(1, N+1)}
    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u][v] = w
    start, end = map(int, sys.stdin.readline().split())
    distances = dijkstra(graph, start)

    print(distances[end])
