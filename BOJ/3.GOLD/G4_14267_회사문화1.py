# G4 14267 회사 문화 1
# https://www.acmicpc.net/problem/14267
# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 트리에서의 다이나믹 프로그래밍
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
employee = [[] for _ in range(n+1)]
for i, num in enumerate(lst[1:]):
    employee[num].append(i+2)

com = {}
for _ in range(m):
    i, w = map(int, input().split())
    if i in com.keys():
        com[i] += com[i] + w
    else:
        com[i] = w

for k, v in com.values():
    print(k, v)

# score = [0]*(n+1)
# for _ in range(m):
#     i, w = map(int, input().split())
#     deq = deque()
#     deq.append(i)
#     while deq:
#         tmp = deq.popleft()
#         deq += employee[tmp]
#         score[tmp] += w
# print(*score[1:])