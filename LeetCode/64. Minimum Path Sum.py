class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #setting
        row = len(grid)
        col = len(grid[0])
        
        #dp table
        dp = []
        dp.append([])
        dp[0].append(grid[0][0])  
        
        #fill up with <row = 0>
        for i in range (1, col):
            dp[0].append(dp[0][i - 1] + grid[0][i])
            
        #fill up with <col = 0>
        for j in range (1, row):
            dp.append([])
            dp[j].append(dp[j - 1][0] + grid[j][0])
        
        #other part
        for i in range(1, row): #rows
            for j in range(1, col): #cols
                dp[i].append(min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]) 
        
        return dp[row - 1][col - 1]
