# G3 16562 친구비
# https://www.acmicpc.net/problem/16562
# 그래프 이론, 자료 구조, 그래프 탐색, 분리 집합

import sys
input = sys.stdin.readline


def union(a, b):
    a = find(a)
    b = find(b)
    if A[a] < A[b]:                       # 부모를 친구비가 더 작은 걸로 저장.
        parent[b] = a
    else:
        parent[a] = b


def find(c):     # 부모 찾기
    if parent[c] != c:    # 자기 자신이 아니라면 재귀 돌면서 부모 찾기.
        parent[c] = find(parent[c])             # 찾은 부모를 저장
    return parent[c]


N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
parent = [i for i in range(N + 1)]   # 부모를 저장
for _ in range(M):
    x, y = map(int, input().split())
    union(x, y)

money = 0
for i in range(1, N+1):              # 부모가 다 연결 안되어있을 수 있으므로 돌면서 다시 부모 찾기
    if parent[i] == i:
        money += A[i]
if money <= K:
    print(money)
else:
    print("Oh no")

