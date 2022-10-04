class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parent = [-1]*n
        for i in range(n):
            self.parent[i] = i
    
    def find(self, i):
	#Path Compression
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            self.parent[yroot]= xroot
    
    def get_count(self):
        total = set()
        print(self.parent)
        for i in range(self.n):
            total.add(self.find(i))
        print("total", total)
        return len(total)


class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        #Union-Find Solution
        n = len(M[0])
        uf = UnionFind(n)
        
        for r in range(len(M)):
            for c in range(len(M[0])):
                if M[r][c] == 1:
                    uf.union(r,c)
        
        return uf.get_count()
        
