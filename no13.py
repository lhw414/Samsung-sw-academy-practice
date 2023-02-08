import sys
sys.stdin = open("input.txt", "r")

def check(y, x):
    global N
    direction = [0, 0, 0, 0]
    for d in range(4):
        now_y, now_x = y, x
        length = 0
        while 0 < now_y < N-1 and 0 < now_x < N-1:
            length +=1
            now_y = now_y + dy[d]
            now_x = now_x + dx[d]
            if arr[now_y][now_x]:
                break
        else:
            direction[d] = length
    return direction

def connect(y, x, d):
    global N
    now_y, now_x = y, x
    while 0 < now_y < N-1 and 0 < now_x < N-1:
        now_y = now_y + dy[d]
        now_x = now_x + dx[d]
        arr[now_y][now_x] = arr[now_y][now_x] ^ 1

def dfs(cur, min_sum, result_cnt):
    global result
    if result_cnt > result[0]:
        result[0] = result_cnt
        result[1] = min_sum
    elif result_cnt == result[0]:
        if result[1] > min_sum:
            result[1] = min_sum
    if cur == cnt:
        return
    y, x = core[cur][0], core[cur][1]
    direction = check(y, x)
    for d in range(4):
        if direction[d] == 0:
            continue
        connect(y, x, d)
        dfs(cur + 1, min_sum + direction[d], result_cnt + 1)
        connect(y, x, d)
    dfs(cur + 1, min_sum, result_cnt)



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    core = []
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j] == 1:
                core.append([i,j])
                cnt = cnt+1
    result = [0, 0] # 개수, 총길이
    dfs(0, 0, 0)
    print(f'#{test_case} {result[1]}')
    
