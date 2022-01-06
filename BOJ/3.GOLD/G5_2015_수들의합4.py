# G5 2015 수들의 합 4
# https://www.acmicpc.net/problem/2015
# 자료 구조, 누적 합, 트리를 사용한 집합과 맵
# 시간초과!

from itertools import accumulate
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))
num = 0
for i in range(N):
    temp = A[i:]
    prefix_sum = list(accumulate(temp))
    num += prefix_sum.count(K)
print(num)
