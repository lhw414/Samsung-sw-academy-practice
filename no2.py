T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    binaryM = bin(M)
    ans = "ON"
    for i in range(1, N+1):
        if(binaryM[-i]!="1"):
            ans = "OFF"
            break
    ansLine = "#" + str(test_case) + " " + ans
    print(ansLine)
