import sys
from math import *
#input = sys.stdin.readline

def update(node, start, end, idx, val):
    if idx < start or end < idx:
        return
    if start == end:
        tree[node] = val
        return
    mid = (start + end) // 2
    update(node*2, start, mid, idx, val)
    update(node*2 + 1, mid+1, end, idx, val)
    tree[node] = (tree[node*2] * tree[node*2 + 1]) % 1000000007

def query(node, start, end, left, right):
    if right < start or end < left:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    temp = query(node*2, start, mid, left, right) * query(node*2 + 1, mid+1, end, left, right)
    return temp % 1000000007

if __name__ == "__main__":
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    
    h = int(ceil(log2(n)))
    t_size = 1 << (h+1)

    arr = list()
    tree = [0] * t_size

    for i in range(n):
        num = int(sys.stdin.readline())
        arr.append(num)
        update(1, 0, n-1, i, num)
    for _ in range(m+k):
        a, b, c = [int(x) for x in sys.stdin.readline().split()]
        #map(int, input().split())
        if a == 1:
            arr[b-1] = c
            update(1, 0, n-1, b-1, c)
        elif a == 2:
            print(query(1, 0, n-1, b-1, c-1))
