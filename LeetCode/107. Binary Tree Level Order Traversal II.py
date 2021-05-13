# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.tree = []
        self.index = 0
        
    def get_height(self, root):
        if root == None:
            return 0
        l_height = self.get_height(root.left)
        r_height =  self.get_height(root.right)
        #get more deeper
        if l_height < r_height:
            return r_height + 1
        return l_height + 1
    
    
    def excute(self, root, level):
        if root is None:
            return 
        if level == 1:
            self.tree[self.index].append(root.val)
        elif level > 1:
            self.excute(root.left, level - 1)
            self.excute(root.right, level - 1)
    
    def level_order(self, root):
        height = self.get_height(root)
        for level in range(height, 0, -1):
            self.tree.append([])
            self.excute(root, level)
            self.index += 1
    
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.level_order(root)
        return self.tree
