# S4 23038 박스 그림 문자
# https://www.acmicpc.net/problem/23038
# 미완성..
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# box = list(list(input().rstrip()) for _ in range(3*N))


def check(n, m):
    r, c = 3*n, 3*m
    flag = False
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nr >= 3*N or nc < 0 or nc >= 3*N or box[nr][nc] == '.':
            continue
        flag = True
        box[r+dx[d]][c+dy[d]] = '#'
    if flag:
        box[r+1][c+1] = '#'

# print(box)
dr, dc, dx, dy = (-1, 1, 1, 3), (1, -1, 3, 1), (0, 1, 1, 2), (1, 0, 2, 1)
for n in range(N):
    for m in range(M):
        if not (n + m) % 2:
            continue
        print(n, m,3*n, 3*m)

        # check(n, m)

# for n in range(3*N):
#     for m in range(3*M):
#         print(box[n][m], end='')
#     print()
