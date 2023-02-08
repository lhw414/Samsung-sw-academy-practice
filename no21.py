T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    stuff = [[0,0]]
    knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

    for _ in range(N):
        stuff.append(list(map(int, input().split())))



    for i in range(1, N + 1):
        for j in range(1, K + 1):
            weight = stuff[i][0] 
            value = stuff[i][1]
       
            if j < weight:
                knapsack[i][j] = knapsack[i - 1][j]
            else:
                knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
    print("#{0} {1}".format(test_case, knapsack[N][K]))
