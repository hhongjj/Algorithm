# G4 10836 여왕벌
# https://www.acmicpc.net/problem/10836
# 구현, 시뮬레이션
from collections import deque

M, N = map(int, input().split())
days = list(list(map(int, input().split())) for _ in range(N))
beehive = [[1] * M for _ in range(M)]
# sizing = [[0] * M for _ in range(M)]

print(beehive)
for i in range(N):
    pass