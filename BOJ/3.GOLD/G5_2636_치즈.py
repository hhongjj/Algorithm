# G5 2636 치즈
# https://www.acmicpc.net/problem/2636
# 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
now_cheese, cnt = 0, 0
cheese = []
for _ in range(N):
    temp = list(map(int, input().split()))
    now_cheese += sum(temp)
    cheese.append(temp)

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
def bfs(sx, sy):
    global now_cheese
    visited = list([0] * M for _ in range(N))
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny]:
                continue
            visited[nx][ny] = 1
            if cheese[nx][ny]:
                cheese[nx][ny] = 0
                now_cheese -= 1
            else:
                q.append((nx, ny))


while now_cheese:
    last_cheese = now_cheese
    cnt += 1
    bfs(0, 0)

print(cnt)
print(last_cheese)
