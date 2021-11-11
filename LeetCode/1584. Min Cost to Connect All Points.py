class Solution(object):
    def __init__(self):
        self.graph = {}
        self.parent = []
        
    def makeGraph(self, points):
        E = []
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j: continue
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                E.append((i, j, dis))
        return E
    
    def find(self, x):
        if self.parent[x] == x: return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x < y: self.parent[y] = x
        else: self.parent[x] = y
            
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        edges = self.makeGraph(points)
        self.parent = [i for i in range(len(points))]
        edges = sorted(edges, key=lambda x: x[2])

        ans = 0
        cntE = 0
        idx = 0
        while cntE < len(points) - 1:
            if self.find(edges[idx][0]) != self.find(edges[idx][1]):
                self.union(edges[idx][0], edges[idx][1])
                print(edges[idx][0], edges[idx][1])
                ans += edges[idx][2]
                cntE += 1
            idx += 1
        return ans
