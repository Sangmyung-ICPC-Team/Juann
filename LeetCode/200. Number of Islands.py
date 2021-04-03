class Solution(object):
    def depth_first_search(self, grid, x, y, m, n):
        if x < 0 or x >= m or y < 0 or y >= n:
            return False
        if grid[x][y] == '1':
            grid[x][y] = '0'
            self.depth_first_search(grid, x + 1, y, m, n)
            self.depth_first_search(grid, x - 1, y, m, n)
            self.depth_first_search(grid, x, y + 1, m, n)
            self.depth_first_search(grid, x, y - 1, m, n)
            return True
        return False
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if self.depth_first_search(grid, i, j, m, n):
                    cnt +=1
        return cnt
