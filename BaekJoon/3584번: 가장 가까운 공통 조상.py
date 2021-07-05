import sys
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    p_list = [0 for _ in range(N+1)] #save parent node of each node

    for _ in range(N - 1):
        u, v = map(int, sys.stdin.readline().split())
        p_list[v] = u #save parent node
    
    u, v = map(int, sys.stdin.readline().split())
    u_parent = [u]
    v_parent = [v]

    while p_list[u]:
        u_parent.append(p_list[u])
        u = p_list[u]
    
    while p_list[v]:
        v_parent.append(p_list[v])
        v = p_list[v]

    u_level = len(u_parent) - 1
    v_level = len(v_parent) - 1

    while u_parent[u_level] == v_parent[v_level]:
        u_level -= 1
        v_level -= 1
    
    print(u_parent[u_level + 1])
