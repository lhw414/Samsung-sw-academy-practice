T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    s1 = set()
    s1Arr = list(input().split())
    s2Arr = list(input().split())
    ans = 0
    for string in s1Arr:
        s1.add(string)
    for string in s2Arr:
        if string in s1:
            ans += 1
    print('#{0} {1}'.format(test_case, ans))