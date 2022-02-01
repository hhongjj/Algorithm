# B5 2475 검증수
# https://www.acmicpc.net/problem/2475
# 수학, 구현, 사칙연산

import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))
num = 0
for l in lst:
    num += l*l

print(num % 10)
