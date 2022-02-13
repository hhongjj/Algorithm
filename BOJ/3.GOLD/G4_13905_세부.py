# G4 13905 세부
# https://www.acmicpc.net/problem/13905
# 그래프 이론, 자료 구조, 그래프 탐색, 이분 탐색, 분리 집합, 최소 스패닝 트리

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s, e = map(int, input().split())
dari = list([] for _ in range(N+1))
for _ in range(M):
    a, b, c = map(int, input().split())
    dari[a].append([b, c])
    dari[b].append([a, c])


def pepero(weight):
    queue = deque()
    queue.append(s)
    visited = [0] * (N+1)
    visited[s] = 1
    while queue:
        now_home = queue.popleft()
        if now_home == e:
            return 1
        for next_home, next_weight in dari[now_home]:
            if not visited[next_home] and weight <= next_weight:
                visited[next_home] = 1
                queue.append(next_home)
    return 0


start, end, result = 1, 1000000, 0
while start <= end:
    mid = (start + end) // 2
    if pepero(mid):
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
