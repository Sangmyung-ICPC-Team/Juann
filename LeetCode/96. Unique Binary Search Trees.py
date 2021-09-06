'''
# <<< Time Limit Exceeded >>> #
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        res = 0
        for i in range(1, n+1):
            #left sub tree * right sub tree
            res += self.numTrees(i-1)*self.numTrees(n-i)
        return res
'''       

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [0]*(n+1)
        arr[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                arr[i] += arr[j-1] * arr[i-j]
        return arr[-1]
