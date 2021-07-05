# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def depth_first_search(self, root, string, arr):
        if root:
            string += str(root.val)
            self.depth_first_search(root.left, string, arr)
            self.depth_first_search(root.right, string, arr)
            if root.left == None and root.right == None:
                arr.append(string)
            
            
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        string = ""
        arr = list()
        self.depth_first_search(root, string, arr)

        for i in range(len(arr)):
            arr[i] = int(arr[i])
        return sum(arr)
