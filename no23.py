#import sys
#sys.stdin = open("input.txt", "r")

class MaxHeap(object):

    def __init__(self):
        self.queue = []
    
    def insert(self, n):
        self.queue.append(n)
        last_index = len(self.queue) - 1
        while 0<=last_index:
            parent_index = self.parent(last_index)
            if 0<=parent_index and self.queue[parent_index] < self.queue[last_index]:
                self.swap(last_index, parent_index)
                last_index = parent_index
            else:
                break

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index < 0:
            return -1
        self.swap(0, last_index)
        maxV = self.queue.pop()
        self.maxHeapify(0)
        return(maxV)
        
    def maxHeapify(self, i):
        left_index = self.leftchild(i)
        right_index = self.rightchild(i)
        max_index = i
        if left_index <= len(self.queue) -1 and self.queue[max_index] < self.queue[left_index]:
            max_index = left_index
        if right_index <= len(self.queue) -1 and self.queue[max_index] < self.queue[right_index]:
            max_index = right_index
        
        if max_index != i:
            self.swap(i, max_index)
            self.maxHeapify(max_index)

    def leftchild(self, i):
        return i*2 + 1

    def rightchild(self, i):
        return i*2 + 2
    
    def parent(self, index):
        return (index-1) // 2
    
    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    heap = MaxHeap()
    ans = []
    for i in range(N):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            heap.insert(cmd[1])
        else:
            ans.append(heap.delete())
    print("#{0}".format(test_case), end="")
    for answer in ans:
        print(" {0}".format(answer), end="")
    print()