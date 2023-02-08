T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    checkAns = 0b0000000000
    N = int(input())
    nowN = N
    while (checkAns != 0b1111111111):
        for char in str(N):
            checkAns |= (1<<int(char))
        nowN += N
    nowN -= N
    answer = "#" + str(test_case) + " " + str(nowN)
    print(answer)
        


