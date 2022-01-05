# S3 11659 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659
# 누적 합

from itertools import accumulate
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
N_list = list(map(int, input().split()))
prefix_sum = [0] + list(accumulate(N_list))
for _ in range(M):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s - 1])
