import sys
sys.setrecursionlimit(10 ** 6)

def create_dict(V):
    graph = dict()
    visited = dict()
    for i in range(1, V + 1):
        visited[i] = 0
        graph[i] = list()
    return graph, visited

def depth_first_search(graph, visited, vtx, color):
    visited[vtx] = color
    for idx in graph[vtx]:
        if visited[idx] == 0:
            if not depth_first_search(graph, visited, idx, -color):
                return False
        elif visited[idx] == visited[vtx]: #same color
            return False
    return True

if __name__ == "__main__":
    testCase = int(sys.stdin.readline())

    for _ in range(testCase):
        V, E = map(int , sys.stdin.readline().split())
        graph, visited = create_dict(V) #create dictionary for adj_list graph 

        for _ in range(E):
            u, v = map(int, sys.stdin.readline().split())
            graph[u].append(v)
            graph[v].append(u)
        
        for idx in range(1, V+1):
            if visited[idx] == 0:
                flag = depth_first_search(graph, visited, idx, 1)
                if  not flag:
                    print("NO")
                    break
        if flag:
            print("YES")
