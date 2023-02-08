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
        for i in range(index-1):
            currNode = currNode.next
        currNode.next = currNode.next.next


T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    length = int(input())
    cryptogram = list(input().split())

    nowLinkedList = LinkedList(cryptogram[0])
    for i in range(1, length):
        nowLinkedList.append(cryptogram[i])

    numCommand = int(input())
    commandList = list(input().split())

    currIndex = 0
    for i in range(numCommand):
        if(commandList[currIndex] == "I"):
            currIndex += 1
            x = int(commandList[currIndex])
            currIndex += 1
            y = commandList[currIndex]
            for j in range(int(y)):
                currIndex += 1
                nowLinkedList.insert(int(commandList[currIndex]), x)
                x += 1
            currIndex += 1

        elif(commandList[currIndex] == "D"):
            currIndex += 1
            x = int(commandList[currIndex])
            currIndex += 1
            y = commandList[currIndex]
            for j in range(int(y)):
                nowLinkedList.delete(x)
                # x += 1
            currIndex += 1

        elif(commandList[currIndex] == "A"):
            currIndex += 1
            y = commandList[currIndex]
            for j in range(int(y)):
                currIndex += 1
                nowLinkedList.append(int(commandList[currIndex]))
            currIndex += 1

    ansLine = "#" + str(test_case)
    currentNode = nowLinkedList.head
    for i in range(10):
        ansLine += " " + str(currentNode.data)
        currentNode = currentNode.next
    print(ansLine)



