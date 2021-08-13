# 2178 미로 탐색

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
maze = []
deq  = deque((1,1))
for i in range(N):
    maze.append(list(map(int,input().rstrip())))


i, j = 0, 0
cnt = 1

def deq_push(deq, i, j):
    deq.append((i,j))
    return deq, i ,j

def deq_pop(deq, i, j):
    deq.pop()
    return deq, i, j

while 1:
    if i+1 == N and j+1 == M:
        break
    if j+1 < M and maze[i][j+1] == 1:
        deq, i, j = deq_push(deq, i, j+1)
        cnt += 1
    elif i+1 < N and maze[i+1][j] == 1:
        deq, i, j = deq_pop(deq, i+1, j)
        deq.append((i+1,j))
        cnt += 1
    else:
        i, j = deq.pop()



print(deq)
print(cnt)

# while 1:
#     if i+1 == N and j+1 == M:
#         break
#     if j+1 < M and maze[i][j+1] == 1:
#         j += 1
#         deq_push((i,j+1))
#         cnt += 1
#     elif i+1 < N and maze[i+1][j] == 1:
#         deq.append((i+1,j))
#         cnt += 1
#     else:
#         deq.pop()