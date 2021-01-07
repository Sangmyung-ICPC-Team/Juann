n = int(input())
parents = list(map(int, input().split()))
del_node = int(input())

tree = {} #dictionary 

for i in range(n):
    #self or child node
    if i == del_node or parents[i] ==del_node:
        continue
    if parents[i] in tree:
        tree[parents[i]].append(i)
    else:
        tree[parents[i]] = [i] #key(self.parent) = value(index)

res = 0 #count number of tree
if -1 in tree:
    que = [-1]
else:
    que = []
while que:
    node = que.pop()
    if node not in tree:
        res += 1
    else:
        que += tree[node]

print(res)
