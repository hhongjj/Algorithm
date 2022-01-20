# S1 18405 경쟁적 전염
# https://www.acmicpc.net/problem/18405
# 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
virus = []
pos = []
for i in range(N):
    tmp = list(map(int, input().split()))
    virus.append(tmp)
    if sum(tmp):
        for j in range(N):
            if tmp[j]:
                pos.append((tmp[j], i, j))

S, X, Y = map(int, input().split())
if virus[X-1][Y-1]:
    print(virus[X-1][Y-1])
else:
    pos.sort(key=lambda x: x[0])
    pos = deque(pos)
    dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
    while S:
        tmp = deque()
        while pos:
            k, x, y = pos.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= N or virus[nx][ny]:
                    continue
                virus[nx][ny] = k
                tmp.append((k, nx, ny))
        pos = tmp
        S -= 1

    print(virus[X-1][Y-1])





