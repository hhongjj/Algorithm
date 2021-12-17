# G4 1647 도시 분할 계획
# https://www.acmicpc.net/problem/1647
# 그래프 이론, 최소 스패닝 트리
import operator
N, M = map(int, input().split())
edge = list(list(map(int, input().split())) for _ in range(M))
edge.sort(key=lambda x: x[2])
# edge.sort(key=operator.itemgetter(2))
print(edge)
