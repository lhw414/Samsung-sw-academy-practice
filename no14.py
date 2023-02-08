from collections import deque
import sys
import copy
sys.stdin = open("input.txt", "r")

def makeNumspace(y, x):
    global N
    tmp = 0
    for d in range(8):
        new_y, new_x = y + dy[d], x + dx[d]
        if 0<=new_x<N and 0<=new_y<N and arr[new_y][new_x] == "*":
            tmp = tmp+1
    num_arr[y][x] = tmp

def bfs(y, x):
    Q = deque()
    Q.append([y, x])
    num_arr[y][x] = "*"

    while Q:
        now_y, now_x = Q.popleft()
        for d in range(8):
            new_x, new_y = now_x + dx[d], now_y + dy[d]
            if 0<=new_x<N and 0<=new_y<N:
                if num_arr[new_y][new_x] == 0:
                    num_arr[new_y][new_x] = "*"
                    Q.append([new_y, new_x])

                elif num_arr[new_y][new_x] != "*":
                    num_arr[new_y][new_x] = "*"

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    num_arr = [item[:] for item in arr]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if num_arr[i][j] == ".":
                makeNumspace(i, j)
    for i in range(N):
        for j in range(N):
            if num_arr[i][j] == 0:
                cnt = cnt + 1
                bfs(i, j)
    for i in range(N):
        for j in range(N):
            if num_arr[i][j] != "*":
                cnt = cnt+1

    print(f'#{test_case} {cnt}')