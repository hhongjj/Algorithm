# G4 1197 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197
# 그래프 이론, 최소 스패닝 트리

V, E = map(int, input().split())
edge = list(list(map(int, input().split())) for _ in range(E))
