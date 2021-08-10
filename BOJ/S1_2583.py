# S1 2583 영역 구하기
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

M, N, K = map(int, input().split())
domain = [[0]*N for _ in range(M)]
visited = [[0]*N for _ in range(M)]
for case in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(M-d, M-b):
        for j in range(a, c):
            domain[i][j] = 1
K_list =[]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(M):
    for j in range(N):
        w = 1
        if domain[i][j] or visited[i][j] :
            continue
        stack = [[i, j]]
        visited[i][j] = 1
        while stack:
            p, q = stack.pop()
            for d in range(4):
                x = p + dx[d]
                y = q + dy[d]
                if 0 <= x < N and 0 <= y < M and not domain[x][y] and not visited[x][y]:
                    stack.append([x,y])
                    visited[x][y] = 1
                    w += 1
        K_list.append(w)

print(K_list)


