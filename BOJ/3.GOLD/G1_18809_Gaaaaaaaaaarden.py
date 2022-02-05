# G1 18809 Gaaaaaaaaaarden
# https://www.acmicpc.net/problem/18809
# 구현, 그래프 이론, 브루트포스 알고리즘, 그래프 탐색, 너비 우선 탐색, 시뮬레이션
# 시간초과.... 
import sys, copy
from itertools import permutations
from collections import deque
input = sys.stdin.readline

N, M, G, R = map(int, input().split())
garden, pos, result = [], [], []
if not G or not R:
    print(0)
    exit()
for i in range(N):
    temp = list(map(int, input().split()))
    if 2 in temp:
        for j in range(M):
            if temp[j] == 2:
                pos.append([i, j])
    garden.append(temp)
pos = list(permutations(pos, G+R))
# print(pos)
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
def bfs(stack):
    cnt = 0
    # print(stack)
    visited = [[0] * M for _ in range(N)]
    run = 0
    while stack:
        temp = deque(copy.deepcopy(stack))
        stack = []
        run += 1
        while temp:

            x, y = temp.popleft()
            num = gd[x][y]
            if num == -1:
                continue
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if nx < 0 or nx >= N or ny < 0 or ny >= M or gd[nx][ny] <= 0 or gd[nx][ny] == num or visited[nx][ny] > run:
                    continue

                if gd[nx][ny] == 1 or gd[nx][ny] == 2:
                    gd[nx][ny] = num
                    visited[nx][ny] = run
                    stack.append([nx, ny])
                    # visited[nx][ny] += 1
                # elif visited[nx][ny] == visited[x][y]:
                elif visited[nx][ny] == run:
                    gd[nx][ny] = -1   # 꽃
                    cnt += 1
    # print(visited)
    result.append(cnt)


while pos:
    temp = pos.pop()
    gd = copy.deepcopy(garden)
    g = G
    for x, y in temp:
        if g:
            gd[x][y] = 3
            g -= 1
        else:
            gd[x][y] = 4
    bfs(deque(temp))
    # print(gd)
    # print(result)

print(max(result))

