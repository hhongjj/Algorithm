# G5 16938 캠프준비
# https://www.acmicpc.net/problem/16938
# 수학, 브루트포스 알고리즘,조합론,비트마스킹,백트래킹
# import sys
from itertools import combinations

# input = sys.stdin.readline
N, L, R, X = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = []
for i in range(2, N+1):
    B.append(list(combinations(A, i)))

result = []
for _ in range(len(B)):
    q = B.pop()
    while q:
        tmp = q.pop()
        if R >= sum(tmp) >= L and tmp[-1] - tmp[0] >= X:
                result.append(tmp)

print(len(result))




