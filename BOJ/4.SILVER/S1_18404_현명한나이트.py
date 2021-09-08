# S1 18404 현명한 나이트
# 그래프 이론, 그래프 탐색, 너비 우선 탐색
# 시간 초과....
import sys
from collections import deque
input = sys.stdin.readline


def bfs(N, sr, sc, er, ec):
    visited = [[0] * N for _ in range(N)]
    stack = deque()
    stack.append((sr, sc, 0))
    visited[sr][sc] = 1
    dr = [-1, -2, -2, -1, 1, 2, 2, 1]
    dc = [-2, -1, 1, 2, 2, 1, -1, -2]
    while stack:
        r, c, n = stack.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N or visited[nr][nc]:
                continue
            if nr == er and nc == ec:
                return n + 1
            visited[nr][nc] = 1
            stack.append((nr, nc, n + 1))


N, M = map(int, input().split())     # N x N 체스판, M개의 상대편 말
X, Y = map(int, input().split())     # 나이트의 위치

for _ in range(M):
    A, B = map(int, input().split())
    res = bfs(N, X-1, Y-1, A-1, B-1)
    print(res, end=' ')


