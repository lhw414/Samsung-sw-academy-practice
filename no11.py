import sys
sys.stdin = open("input.txt", "r")

def calcTreeSize(anchester: int, numEdge, edges):
    size.append(anchester)
    for i in range(0, 2*numEdge, 2):
        if edges[i] == anchester:
            calcTreeSize(edges[i+1], numEdge, edges)

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    numNode, numEdge, nodeA, nodeB = map(int, input().split())
    edges = list(map(int, input().split()))
    dicEdge = {}
    nodeAAnchester = [nodeA,]
    nodeBAnchester = [nodeB,]
    Anchester = None

    for i in range(numEdge):
        dicEdge[edges[i*2+1]] = edges[i*2]

    while(nodeAAnchester[-1] != 1):
        nodeAAnchester.append(dicEdge[nodeAAnchester[-1]])
    
    while(nodeBAnchester[-1] != 1):
        for node in nodeAAnchester:
            if(node == dicEdge[nodeBAnchester[-1]]):
                Anchester = node
                break
        nodeBAnchester.append(dicEdge[nodeBAnchester[-1]])
        if(Anchester is not None):
            break
    size = []
    Anchester = int(Anchester)
    calcTreeSize(Anchester, numEdge, edges)
    print(f'#{test_case} {Anchester} {len(size)}')
