N = int(input()) #number of node

tree = {}
for _ in range(N):
    parent, child1, child2 = map(int, input().split())
    tree[parent] = [child1, child2]

#number of node in left subtree

#number of node in right subtree

#height of left subtree

#height of left subtree