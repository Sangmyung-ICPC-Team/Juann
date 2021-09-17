import sys
#재귀 깊이 설정
sys.setrecursionlimit(10**6) 
#트리에 달릴 노드 Class
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

#노드의 집합 -> 트리 Class
class SearchTree:
    def __init__(self):
        self.root = None
        
    def insertNode(self, data): #Node insert 함수
        newNode = Node(data) 
        if self.root == None:
            self.root = newNode
        
        node = self.root
        while True:
            preNode = node
            if node.data[0] > newNode.data[0]:
                node = node.left
                if node == None:
                    node = newNode
                    preNode.left = node
            elif node.data[0] < newNode.data[0]:
                node = node.right
                if node == None:
                    node = newNode
                    preNode.right = node
            else: return
    def preOrder(self, tree, nodeinfo, answer):
        if tree:
            answer.append(nodeinfo.index(tree.data) + 1)
            self.preOrder(tree.left, nodeinfo, answer)
            self.preOrder(tree.right, nodeinfo, answer)
    def postOrder(self, tree, nodeinfo, answer):
        if tree:
            self.postOrder(tree.left, nodeinfo, answer)
            self.postOrder(tree.right, nodeinfo, answer)   
            answer.append(nodeinfo.index(tree.data) + 1)
            
def solution(nodeinfo):
    answer = []
    Tree = SearchTree()
    temp = sorted(nodeinfo, key=lambda x: x[1], reverse=True)
        
    #Create Tree
    for node in temp:
        Tree.insertNode(node)
        
    Tanswer = []
    Tree.preOrder(Tree.root, nodeinfo, Tanswer)
    answer.append(Tanswer)
    
    Tanswer = []
    Tree.postOrder(Tree.root, nodeinfo, Tanswer)
    answer.append(Tanswer)

    #Preorder Traversal 
    #Postorder Traversal
    
    return answer
