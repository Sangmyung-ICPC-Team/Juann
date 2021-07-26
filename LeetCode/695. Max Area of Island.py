class Solution(object):
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, 1, -1]

    def depth_first_search(self, grid, row, col, curr_x, curr_y, visited):
        if row <= curr_x or curr_x < 0 or col <= curr_y or 0 > curr_y:
            return 0
        if grid[curr_x][curr_y] == 1 and visited[curr_x][curr_y] == False:
            cnt = 0
            visited[curr_x][curr_y] = True
            for i in range(4):
                cnt += self.depth_first_search(grid, row, col, curr_x+self.dx[i], curr_y+self.dy[i], visited)
            return cnt + 1
        return 0
            
        
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        visited = [[False for _ in range(col)] for _ in range(row)]
        
        answer = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    temp = self.depth_first_search(grid, row, col, i, j, visited)
                    if answer < temp:
                        answer = temp
        return answer
