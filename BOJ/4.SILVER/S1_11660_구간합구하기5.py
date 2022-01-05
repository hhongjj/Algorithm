# S1 11660 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660
# 다이나믹 프로그래밍, 누적합

from itertools import accumulate
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
zero = [[0 for _ in range(N+1)]]
lst = zero + list([0] + list(map(int, input().split())) for _ in range(N))
prefix_sum = [list(accumulate(i)) for i in lst]
for i in range(1, len(prefix_sum)):
    for j in range(len(prefix_sum)):
        prefix_sum[i][j] += prefix_sum[i-1][j]

for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    print(prefix_sum[ex][ey] - prefix_sum[sx - 1][ey] - prefix_sum[ex][sy - 1] + prefix_sum[sx - 1][sy - 1])
