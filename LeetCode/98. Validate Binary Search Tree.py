# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, arr):
        if root:
            self.inorder(root.left, arr)
            arr.append(root.val)
            self.inorder(root.right, arr)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        arr = [] #is it sorted?
        self.inorder(root, arr)
        
        #func. all? 인자로 주어진 리스트의 모든 요소가 true일 때, true를 반환 
        #시간 복잡도 sorted보다 20배 빠름.
        if all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)):
            return True
        return False
