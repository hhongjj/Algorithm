# S4 1783 병든 나이트
# https://www.acmicpc.net/problem/1783
# 구현, 그리디 알고리즘, 많은 조건 분기
# 틀림.

import sys
from collections import deque
input = sys.stdin.readline


def check_small():
    stack = deque()
    stack.append((0, 0))
    knight[0][0] = 1
    num = 1
    while stack:
        r, c = stack.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if knight[nr][nc] < knight[r][c] + 1:
                stack.append((nr, nc))
                knight[nr][nc] = knight[r][c] + 1
            if num < knight[nr][nc]:
                num = knight[nr][nc]
    return num


def check_big():
    stack = deque()
    stack.append((0, 0))
    knight[0][0] = 1
    num = 1
    for i in range(4):
        r, c = stack.popleft()
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if knight[nr][nc] < knight[r][c] + 1:
            stack.append((nr, nc))
            knight[nr][nc] = knight[r][c] + 1
        if num < knight[nr][nc]:
            num = knight[nr][nc]
    if not len(stack):
        stack.append((r, c))
    while stack:
        r, c = stack.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if knight[nr][nc] < knight[r][c] + 1:
                stack.append((nr, nc))
                knight[nr][nc] = knight[r][c] + 1
            if num < knight[nr][nc]:
                num = knight[nr][nc]
    return num


N, M = map(int, input().split())


dc = [1, 1, 2, 2]
dr = [2, -2, 1, -1]

if M <= 4:
    N = 2 * M
    knight = [[0] * M for _ in range(N)]
    res = check_small()
    print(res)
else:
    N = 3
    knight = [[0] * M for _ in range(N)]
    res = check_big()
    print(res)

