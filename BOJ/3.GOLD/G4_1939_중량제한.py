# G4 1939 중량제한
# https://www.acmicpc.net/problem/1939
# 그래프 이론, 자료 구조, 그래프 탐색, 이분 탐색, 너비 우선 탐색, 분리 집합

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dari = list([] for _ in range(N+1))
for _ in range(M):
    a, b, c = map(int, input().split())
    dari[a].append([b,c])
    dari[b].append([a, c])
s, e = map(int, input().split())


def suum(weight):
    queue = deque()
    queue.append(s)
    visited = [0]*(N+1)
    visited[s] = 1
    while queue:
        now = queue.popleft()
        if now == e:
            return 1
        for next, next_w in dari[now]:
            if not visited[next] and weight <= next_w:
                visited[next] = 1
                queue.append(next)
    return 0


start, end, result = 1, 1000000000, 0
while start <= end:
    mid = (start + end) // 2
    if suum(mid):
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)