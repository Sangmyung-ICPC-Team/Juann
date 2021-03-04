def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#init
V, E = map(int, input().split())
parent = [0] * (V + 1)

#init
edges = []
result = 0

#self로 table init
for i in range(1, V + 1):
    parent[i] = i

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

#weight순으로 정렬
edges.sort()

for edge in edges:
    cost, a, b = edge
    #cycle이 발생하지 않는 경우
    if find_parent(parent, a) != find_parent(parent, b):
        #union
        union_parent(parent, a, b)
        result += cost

print(result)
