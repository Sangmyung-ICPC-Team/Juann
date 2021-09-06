# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    #if you wanna replace to max(deletedNode.left) 
    def maxValueLeft(self, root):
        current = root
        while current.right is not None:
            current = current.right
        return current
    
    #if you wanna replace to min(deletedNode.right) 
    def minValueRight(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current
        
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        #search a key Node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else: #if you find a Node
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            
            '''select one'''
            temp = self.maxValueLeft(root.left)
            #temp = minValueRigth(root.right)
            
            root.val = temp.val
            root.left = self.deleteNode(root.left, temp.val)
            
        return root
