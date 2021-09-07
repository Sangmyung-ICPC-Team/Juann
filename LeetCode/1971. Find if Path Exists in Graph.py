class Solution(object):
    def __init__(self):
        self.graph = {}
        self.visited = []
    def createGraph(self, edges, n):
        #Create Graph
        for edge in edges:
            if edge[0] not in self.graph:
                self.graph[edge[0]] = []
            if edge[1] not in self.graph:
                self.graph[edge[1]] = []
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        self.visited = [False for _ in range(n)]
    def depthFirstSearch(self, start, end):
        self.visited[start] = True
        for node in self.graph[start]:
            if node == end:
                return True
            if self.visited[node] is False:
                return self.depthFirstSearch(node, end)
        return False
    def validPath(self, n, edges, start, end):
        """
        :type n: int
        :type edges: List[List[int]]
        :type start: int
        :type end: int
        :rtype: bool
        """
        #Two Solution 
        #1. Graph Traversal (DFS / BFS)
        #2. Union Find
        self.createGraph(edges, n)
        return self.depthFirstSearch(start, end)
    
        
