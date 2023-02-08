import sys
from collections import deque, defaultdict
sys.stdin = open("input.txt", "r")

def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent
    
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    nodes = list(map(int, input().split()))
    graph = defaultdict(list)
    depth = defaultdict(int)
    parent = [0, 0] + nodes
    depth[1] = 0

    for i, x in enumerate(nodes):
        depth[i+2] = depth[x] + 1
        graph[x].append(i+2)

    answer, preNode = 0, 1
    Q = deque([1])
    visit = [False] * (N+2)
    visit[1] = True
    tmp = 0

    while Q:
        node = Q.popleft()
        if node != 1:
            tmp = (depth[node] + depth[preNode] - 2 * depth[lca(node, preNode)])
            answer += tmp
        
        for next_node in graph[node]:
            if not visit[next_node]:
                visit[next_node] = True
                Q.append(next_node)
        
        preNode = node

    print(f"#{test_case} {answer}")
