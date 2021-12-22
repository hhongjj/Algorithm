# G5 2240 자두나무
# https://www.acmicpc.net/problem/2240
# 다이나믹 프로그래밍

T, W = map(int, input().split())
tree = list(map(int, input().split()))
dp = [[0] * W for _ in range(T)]
print(dp)