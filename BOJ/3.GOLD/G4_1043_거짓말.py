# G4 1043 거짓말
# https://www.acmicpc.net/problem/1043
# 그래프 이론, 자료 구조, 그래프 탐색, 분리집합
from collections import deque
import sys
input = sys.stdin.readline


def party():
    global stack
    visited = [0] * M
    while stack:
        x = stack.popleft()
        for k in range(M):
            if visited[k]:
                continue
            if x in people[k][1:]:
                visited[k] = 1
                for y in people[k][1:]:
                    stack.append(y)
        stack = deque(set(stack))

    print(visited)
    return


N, M = map(int, input().split())
lie = list(map(int, input().split()))
people = list(list(map(int, input().split())) for _ in range(M))

if not lie[0]:
    print(M)
elif M == 1 and lie[0]:
    print(0)
else:
    stack = deque()
    for i in lie[1:]:
        stack.append(i)
    party()

