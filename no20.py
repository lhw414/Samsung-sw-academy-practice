T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B = input().split(" ")
    A = " " + A.strip()
    B = " " + B.strip()
    n, m = len(A)-1, len(B)-1
    dp = [[0]*(m+1) for _ in range(n+1)]

    backTrack = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + 1
                backTrack[i][j] = 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print("#{0} {1}".format(test_case, dp[n][m]))