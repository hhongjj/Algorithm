# D3 12716 미로의 거리
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(sr, sc):
    queue = deque()
    visited = [[0] * N for _ in range(N)]
    # sy,sx~ sy,sx의 최소 이동횟수는 0이다. [0]:y좌표,[1]:x좌표 ,[2] : 최소이동횟수
    queue.append((sr, sc, 0))
    # 시작 지점 큐 등록
    visited[sr][sc] = 1

    while queue:
        now = queue.popleft()
        if MAP[now[0]][now[1]] == 3:   # goal
            return now[2] - 1
        for i in range(4):             # next 큐 등록
            nr = now[0] + dr[i]
            nc = now[1] + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if MAP[nr][nc] == 1: continue     #벽
            if visited[nr][nc]: continue  # 방문된것
            visited[nr][nc] = 1          # 재등록 방지
            queue.append((nr, nc, now[2]+1))

    return 0

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    MAP = [list(map(int, input())) for _ in range(N)]
    # 시작 좌표 찾기
    flag = 0
    for r in range(N):
        for c in range(N):
            if MAP[r][c] == 2:
                sr, sc = r, c
                flag = 1
                break
        if flag == 1:
            break
    result = bfs(sr,sc)
    print('#{} {}'.format(tc, result))