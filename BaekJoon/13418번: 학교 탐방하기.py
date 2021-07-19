import sys

def getParent(parent, x):
    if parent[x] == x: return x
    return getParent(parent, parent[x])

def unionParent(parent, node1, node2):
    node1 = getParent(parent, node1)
    node2 = getParent(parent, node2)

    if node1 > node2: parent[node1] = node2
    else: parent[node2] = node1

if __name__ == "__main__":
    building, road = map(int, sys.stdin.readline().split())
    parent_1 = [value for value in range(building + 1)]
    parent_2 = [value for value in range(building + 1)]

    graph = list()
    for _ in range(road+1):
        u, v, w = map(int, sys.stdin.readline().split())
        graph.append([u, v, w])
    

    flag = True
    for i in range(2):
        if i == 0:
            graph.sort(key=lambda item:item[2])
        elif i == 1:
            graph.sort(reverse=True, key=lambda item:item[2])
            parent_1 = parent_2
            flag = False

        cntUpHill = 0 #count how many Uphill in each case
        for edge in graph:
            u, v, w= edge
            if getParent(parent_1, u) != getParent(parent_1, v):
                unionParent(parent_1, u, v)
                if w == 0:
                    cntUpHill += 1
        if flag:
            x = cntUpHill**2
        else:
            y = cntUpHill**2
        
    print(x - y)
