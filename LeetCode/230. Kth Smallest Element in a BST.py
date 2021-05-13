# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.tree = []
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.tree.append(root.val)
            self.inorder(root.right)
            
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder(root)
        return self.tree[k-1]
