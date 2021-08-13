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
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            deq.append([i,j])
    box.append(row)

def bfs(m, n, box):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    count = -1
    while deq:
        count += 1
        for i in range(len(deq)):
            a, b = deq.popleft()
            for j in range(4):
                x = a + dx[j]
                y = b + dy[j]
                if 0 <= x < n and 0 <= y < m and box[x][y] == 0:
                    box[x][y] = 1
                    deq.append([x,y])
    for i in box:
        if 0 in i:
            return -1
    return count

print(bfs(m, n, box))



# 이해했으니 구현을 더 많이 해보도록!

