from collections import deque

class Solution(object):
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, 1, -1]
        
    def where_is_water(self, isWater, rows, cols):
        water_loc = deque()
        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    water_loc.append((i, j))
        return water_loc
    
    def bfs(self, isWater, rows, cols, queue):
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + self.dx[i]
                ny = y + self.dy[i]
                
                if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
                    continue
                if isWater[nx][ny] == 0:
                    queue.append((nx, ny))
                    isWater[nx][ny] = isWater[x][y] + 1
        
    def normalization(self, isWater, rows, cols):
        for i in range(rows):
            for j in range(cols):
                isWater[i][j] -= 1
    
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(isWater), len(isWater[0])
        
        queue = self.where_is_water(isWater, rows, cols)
        self.bfs(isWater, rows, cols, queue)
        self.normalization(isWater, rows, cols)
        
        return isWater
