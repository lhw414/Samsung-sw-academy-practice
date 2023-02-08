T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    s= input()
    pattern = input()

    pattern_hash = hash(pattern)  # 1. 패턴의 hash값을 구한다
    n = len(pattern)
    ans = 0
    initHash = hash(s[0:n])  

    for i in range(len(s)-n+1):
        if i!=0:
            s_hash = 2*(initHash - ord(s[i])) + ord(s[i+n-1])
            initHash = s_hash
        else:
            s_hash = initHash
        if pattern_hash == s_hash:  # 2-2 : 해쉬값이 일치하다면
            if pattern == s[i:i+n]: # 2-2-1 : 패턴과 문자열이 일치한지 확인
                ans += 1

    print('#{0} {1}'.format(test_case, ans))