# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.tree = []
        self.min = 10**5+1
    def traversal(self, root):
        if root:
            self.tree.append(root.val)
            self.traversal(root.left)
            self.traversal(root.right)
    def diff(self, a, b):
        if a > b:
            return a - b
        else:
            return b - a
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.traversal(root)
        self.tree.sort()
        for i in range(len(self.tree) - 1):
            if self.diff(self.tree[i], self.tree[i+1]) < self.min:
                self.min = self.diff(self.tree[i], self.tree[i+1])
        return self.min
