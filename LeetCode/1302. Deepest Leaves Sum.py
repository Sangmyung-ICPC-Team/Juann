# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.sum = 0
    def getDepth(self, root):
        if root:
            return max(self.getDepth(root.right), self.getDepth(root.left)) + 1
        return 0
    def exe(self, root, mDepth, depth):
        if root: # let's find the max depth
            self.exe(root.right, mDepth, depth+1)
            self.exe(root.left, mDepth, depth+1)
            if mDepth == depth: # are you reach the max depth?
                self.sum += root.val
            
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # deepest level (using level order traversal)
        mDepth = self.getDepth(root)
        
        # sumation of its level
        self.exe(root, mDepth, 1)
        
        return self.sum
