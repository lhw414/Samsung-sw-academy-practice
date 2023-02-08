from queue import PriorityQueue

def bfs():
    global ans
    q = PriorityQueue()
    q.put((0, K))
    while q:
        cnt, currNum = q.get()
        if currNum == 0:
            ans = cnt
            break
        q.put((currNum + cnt, 0))
        for num in arr:
            q.put((cnt + currNum%num, currNum//num))
        


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    K = int(input())
    ans = 99999999
    bfs()
    print("#{0} {1}".format(tc, ans))
            
#! BFS에서 queue대신에 PriorityQueue사용하여 시간 단축
#! cnt순으로 정렬하여 작은 cnt가 먼저 pop되도록