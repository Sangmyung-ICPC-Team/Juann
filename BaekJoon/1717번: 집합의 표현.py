def getParent(parent, x):
    if parent[x] == x: return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b: parent[b] = a #small -> big
    else: parent[a] = b

def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b: return True
    return False

import sys
sys.setrecursionlimit(10**5)

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())

    parent = [i for i in range(0 , n+1)]

    for _ in range(m):
        command, a, b = map(int, input().split())
        if command == 0:
            unionParent(parent, a, b)
        elif command == 1:
            if findParent(parent, a, b):
                print("YES")
            else:
                print("NO")
