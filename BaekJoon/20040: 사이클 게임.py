import sys
input = sys.stdin.readline

def getParent(parent, node):
    if parent[node] == node: return node
    parent[node] = getParent(parent, parent[node])
    return parent[node]

def unionParent(parent, node1, node2):
    node1 = getParent(parent, node1)
    node2 = getParent(parent, node2)
    if node1 < node2: parent[node2] = node1
    else: parent[node1] = node2

def findParent(parent, node1, node2):
    node1 = getParent(parent, node1)
    node2 = getParent(parent, node2)
    if node1 == node2:
        return True
    return False

if __name__ == "__main__":
    n, m = map(int, input().split())
    parent = [value for value in range(n)]
    
    flag = False
    temp = 0
    for i in range(m):
        u, v = map(int, input().split())
        if flag == False:
            if findParent(parent, u, v) == True:
                temp = i + 1
                flag = True
            unionParent(parent, u, v)
            if findParent(parent, u, v) == False:
                temp = i + 1
                flag = True
    print(temp)
