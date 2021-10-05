# S1 21608 상어 초등학교
# https://www.acmicpc.net/problem/21608
# 구현
from collections import deque

N = int(input())

lst = list(list(map(int, input().split())) for _ in range(N*N))

pos = [[0]*N for _ in range(N)]

# stack = deque()
# for i in range(len(lst)):
#     stack.append(lst[i][0])

# sn = lst.popleft()
# love = list()
# for i in range(len(lst))
# print(love)

i = 0
sn = lst[i][0]
sr, sc = N//2, N//2
pos[sr][sc] = sn
stu = {sn: (sr, sc)}
i += 1
while i < N:
    nn = lst[i][0]
    for j in range(4):
        pass



