# S1 7576 토마토
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())

visited = [[0]*m for _ in range(n)]
box =[]
deq  = deque()
for i in range(n):
    box.append(list(map(int, input().split())))

def bfs(m, n, box):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]


