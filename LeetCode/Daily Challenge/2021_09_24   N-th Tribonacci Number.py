class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0, 1, 1]
        
        for idx in range(3, n+1):
            memo.append(memo[idx-1] + memo[idx-2] + memo[idx-3])
        return memo[n]
