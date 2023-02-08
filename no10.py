import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    N = int(input())
    dicC = {}
    liTree = [-1 for _ in range(N+1)]
    for i in range(N):
        li_tmp = list(input().split())
        if len(li_tmp) == 4:
            node, op, c1, c2 = li_tmp
            node, c1, c2 = int(node), int(c1), int(c2)
            dicC[node] = (c1, c2)
            liTree[node] = op
        else:
            node, value = li_tmp
            node, value = int(node), float(value)
            liTree[node] = value
    for i in sorted(dicC.keys(), reverse=True):
        if liTree[i] == "+":
            liTree[i] = liTree[dicC[i][0]] + liTree[dicC[i][1]]
        elif liTree[i] == "-":
            liTree[i] = liTree[dicC[i][0]] - liTree[dicC[i][1]]
        if liTree[i] == "*":
            liTree[i] = liTree[dicC[i][0]] * liTree[dicC[i][1]]
        if liTree[i] == "/":
            liTree[i] = liTree[dicC[i][0]] / liTree[dicC[i][1]]
    print("#" + str(test_case) + " " + str(int(liTree[1])))

