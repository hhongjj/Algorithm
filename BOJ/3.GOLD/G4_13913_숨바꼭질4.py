# G4 13913 숨바꼭질 4
# https://www.acmicpc.net/problem/13913
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
visited = [0] * 100001

if N >= K:
    print(N-K)
    for i in range(N, K-1, -1):
        print(i, end=" ")
else:
    lst = deque()
    lst.append([N, 0])
    while lst:
        *x, t = lst.popleft()
        visited[x[-1]] += 1
        a, b, c = x[-1] - 1, x[-1] + 1, 2 * x[-1]
        if 0 <= c <= 100000 and not visited[c]:
            if c == K:
                y = x + [c]
                print(t+1)
                print(*y)
                break
            else:
                y = x + [c, t+1]
                lst.appendleft(y)
        if 0 <= a <= 100000 and not visited[a]:
            if a == K:
                y = x + [a]
                print(t+1)
                print(*y)
                break
            else:
                y = x + [a, t+1]
                lst.append(y)
        if 0 <= b <= 100000 and not visited[b]:
            if b == K:
                y = x + [b]
                print(t+1)
                print(*y)
                break
            else:
                y = x + [b, t + 1]
                lst.append(y)
