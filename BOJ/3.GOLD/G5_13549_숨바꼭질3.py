# G5 13549 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
# 그래프 이론, 자료 구조, 그래프 탐색, 너비 우선 탐색, 다익스트라, 0-1 너비 우선 탐색
import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
visited = [0] * 100001


if N >= K:
    print(N-K)
else:
    lst = deque()
    lst.append((N, 0))
    while lst:
        x, t = lst.popleft()
        visited[x] += 1
        a, b, c = x - 1, x + 1, 2 * x
        if 0 <= c <= 100000 and not visited[c]:
            if c == K:
                print(t)
                break
            else:
                lst.appendleft((c, t))

        if 0 <= a <= 100000 and not visited[a]:
            if a == K:
                print(t+1)
                break
            else:
                lst.append((a, t+1))
        if 0 <= b <= 100000 and not visited[b]:
            if b == K:
                print(t+1)
                break
            else:
                lst.append((b, t+1))

