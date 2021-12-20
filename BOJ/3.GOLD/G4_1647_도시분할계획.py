# G4 1647 도시 분할 계획
# https://www.acmicpc.net/problem/1647
# 그래프 이론, 최소 스패닝 트리

import operator
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
edge = list(list(map(int, input().split())) for _ in range(M))
# edge.sort(key=lambda x: x[2])
edge.sort(key=operator.itemgetter(2))

parents = [i for i in range(0, N+1)]

def find(v):
    if v != parents[v]:
        parents[v] = find(parents[v])
    return parents[v]


def union(a, b):
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


edge_cnt, weight = 0, 0
for e in edge:
    a, b = find(e[0]), find(e[1])
    if a == b:
        continue
    union(a, b)
    edge_cnt += 1
    weight += e[2]
    if edge_cnt == N - 2:
        break
print(weight)


# def union(a, b, w):
#     global edge_cnt, weight
#     a, b = find(a), find(b)
#     if a != b:
#         edge_cnt += 1
#         weight += w
#         if a < b:
#             parents[b] = a
#         else:
#             parents[a] = b
#
# edge_cnt, weight = 0, 0
# for e in edge:
#     union(e[0], e[1], e[2])
#     if edge_cnt == N - 2:
#         break
# print(weight)