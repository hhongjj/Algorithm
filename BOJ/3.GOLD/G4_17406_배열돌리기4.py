# G4 17406 배열 돌리기 4
# https://www.acmicpc.net/problem/17406
# 구현, 브루트포스 알고리즘

import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))

for _ in range(K):
    s, r, c = map(int, input().split())
