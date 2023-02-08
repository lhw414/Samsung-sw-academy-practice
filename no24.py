from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

import sys
sys.stdin = open("input.txt", "r")
T = int(input())

def bfs(arr, visited, time, S, G):
    deq = deque([S])
    while deq:
        x, y = deq.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0<= nx < N and 0 <= ny < N:
                if nx == 0 and ny == 0:
                    continue
                elif visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    time[nx][ny] = time[x][y] + arr[nx][ny]
                    deq.append((nx, ny))
                else:
                    if time[nx][ny] > time[x][y] + arr[nx][ny]:
                        time[nx][ny] = time[x][y] + arr[nx][ny]
                        deq.append((nx, ny))


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T+1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N))

    visited = [[0] * N for _ in range(N)]
    time = [[0] * N for _ in range(N)]
    S, G = [0, 0], [N - 1, N - 1]
    
    bfs(arr, visited, time, S, G)
    answer = time[G[0]][G[1]]
    
    print(f'#{tc} {answer}')
