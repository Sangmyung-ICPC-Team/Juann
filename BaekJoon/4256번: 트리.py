def printpostorder(preorder, inorder):
    N = len(preorder)
    if N == 0: return 

    root = preorder[0] #전위순회의 first traversal은 root이다.
    left_size = inorder.index(root)
    right_size = N - 1 - left_size

    printpostorder(preorder[1:left_size + 1], inorder[0:left_size])
    printpostorder(preorder[left_size+1:N], inorder[left_size+1:N])

    print(root, end=' ')


test_case = int(input())

for _ in range(test_case):
    n = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    printpostorder(preorder, inorder)
    print()
