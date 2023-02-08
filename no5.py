class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        currNode = self.head
        while currNode.next is not None:
            currNode = currNode.next
        currNode.next = Node(data)
    
    def insert(self, data, index):
        currNode = self.head
        newNode = Node(data)
        if(index == 0):
            headNode = self.head
            self.head = newNode
            self.head.next = headNode
            return
        for i in range(index):
            prevNode = currNode
            currNode = currNode.next
        newNode.next = currNode
        prevNode.next = newNode

    def delete(self, index):
        currNode = self.head
        if(index == 0):
            self.head = currNode.next
            return
        for i in range(index-1):
            currNode = currNode.next
        currNode.next = currNode.next.next
    
    def change(self, data, index):
        currNode = self.head
        if(index == 0):
            self.head.data = data
            return
        for i in range(index):
            currNode = currNode.next
        currNode.data = data
    
    def getNodeData(self, index):
        currNode = self.head
        if(index == 0):
            return self.head.data
        for i in range(index):
            if(currNode == None):
                return -1
            currNode = currNode.next
        return currNode.data


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    N, M, L = map(int, input().split())
    cryptogram = list(input().split())

    nowLinkedList = LinkedList(cryptogram[0])
    for i in range(1, N):
        nowLinkedList.append(cryptogram[i])

    for i in range(M):
        commandList = list(input().split())
        if(commandList[0] == "I"):
            nowLinkedList.insert(commandList[2], int(commandList[1]))
        elif(commandList[0] == "D"):
            nowLinkedList.delete(commandList[1])
        elif(commandList[0] == "C"):
            nowLinkedList.change(commandList[2], int(commandList[1]))

    ansLine = "#" + str(test_case) + " " +str(nowLinkedList.getNodeData(int(L)))
    print(ansLine)



