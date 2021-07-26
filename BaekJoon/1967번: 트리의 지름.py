import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]

def depth_first_search(root, weight):
    for node in graph[root]:
        v, w = node
        if distance[v] == -1:
            distance[v] = weight + w
            depth_first_search(v, weight+w)

for _ in range(n-1):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    graph[v].append([u, w])

distance = [-1] * (n+1)
distance[1] = 0 #no.1 node is a root
depth_first_search(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
depth_first_search(start, 0)

print(max(distance))
