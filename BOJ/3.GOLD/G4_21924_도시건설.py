# G4 21924 도시 건설
# https://www.acmicpc.net/group/workbook/view/11808/38334
# 그래프 이론, 최소 스패닝 트리

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N+1)]
doro = list(list(map(int, input().split())) for _ in range(M))
doro.sort(key=lambda x: x[2])


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return 1
    elif a < b:
        parent[b] = a
        return 0
    else:
        parent[a] = b
        return 0


def find(c):
    if parent[c] != c:
        parent[c] = find(parent[c])
    return parent[c]


result = 0
total = 0
for i in range(M):
    x, y, z = doro[i]
    total += z
    if union(x, y):
        continue
    else:
        result += z

for i in range(1, N+1):
    find(i)

if sum(parent) != N:
    print(-1)
else:
    print(total - result)
