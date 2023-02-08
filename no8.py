class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, data):
        self.root = Node(data)
        
    def insert(self, data, index):
        currNode = self.root
        height = -1
        currIndex = index
        while( currIndex != 0 ):
            height = height +1
            currIndex = int(currIndex/2)
        location = index%(pow(2, height))
        for i in range(height):
            if(index%pow(2, height-i) < pow(2, height-i-1)):
                if(currNode.left is None):
                    currNode.left = Node(data)
                    return
                currNode = currNode.left
            elif(index%pow(2, height-i) >= pow(2, height-i-1)):
                if(currNode.right is None):
                    currNode.right = Node(data)
                    return
                currNode = currNode.right
        

        
    def inorder(self, node):
        if node != None:
            if node.left:
                self.inorder(node.left)
            print(node.data, end="")
            if node.right:
                self.inorder(node.right)

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())
    command = list(input().split())
    nowBinaryTree = BinaryTree(command[1])
    for i in range(1, length):
        command = list(input().split())
        nowBinaryTree.insert(command[1], int(command[0]))
    print("#" + str(test_case) + " ", end="")
    nowBinaryTree.inorder(nowBinaryTree.root)
    print("")

