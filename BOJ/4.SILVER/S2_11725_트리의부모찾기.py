# S2 11725 트리의 부모 찾기
# 그래프 이론, 그래프 탐색, 트리, 너비 우선 탐색, 깊이 우선 탐색

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]

visit = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

result = [0] * (N+1)

que = deque()

def find_num(start):
    que.append(start)
    while que:
        x = que.popleft()
        for i in tree[x]:
            if not visit[i]:
                result[i] = x
                que.append(i)
                visit[i] = 1


find_num(1)
for i in range(2, len(result)):
    print(result[i])
