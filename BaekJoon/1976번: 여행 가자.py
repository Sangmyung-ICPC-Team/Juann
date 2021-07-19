import sys
input = sys.stdin.readline

def getParent(city, node):
    if city[node] == node: return node
    city[node] = getParent(city, city[node])
    return city[node]

def unionParent(city, node1, node2):
    node1 = getParent(city, node1)
    node2 = getParent(city, node2)
    if node1 < node2: city[node2] = node1
    else: city[node1] = node2

def findParent(city, node1, node2):
    node1 = getParent(city, node1)
    node2 = getParent(city, node2)
    if node1 == node2: return True
    return False

if __name__ == "__main__":
    N = int(input())
    M = int(input())

    city = [list(map(int, input().split())) for _ in range(N)]
    plan = list(map(int, input().split()))
    parent = [value for value in range(N)]

    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                unionParent(parent, i, j)
    
    S = plan[0] - 1
    for i in range(1, len(plan)):
        if findParent(parent, S, plan[i] - 1) == False:
            print("NO")
            exit()
    print("YES")
