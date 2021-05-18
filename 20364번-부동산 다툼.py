N, Q = map(int, input().split())


#Don't use index(0)
tree = []
for i in range(0, N + 1):
    tree.append([i, False])

def recursion(tree, index, value):
    if index > N:
        return False
    if recursion(tree, index * 2, value):
        return True
    if recursion(tree, (index * 2) + 1, value):
        return True
    if tree[index][1] == True:
        print(tree[index][0])
        return False
    if tree[index][0] == value:
        print(0)
        tree[index][1] = True
        return True
    

for _ in range(Q):
    a = int(input())
    recursion(tree, 1, a)
