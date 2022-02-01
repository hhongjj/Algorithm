# B2 2908 상수
# https://www.acmicpc.net/problem/2908
# 수학, 구현

import sys
input = sys.stdin.readline

num1, num2 = input().split()
print(max(num1[::-1], num2[::-1]))