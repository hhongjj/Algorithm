# G5 2240 자두나무
# https://www.acmicpc.net/problem/2240
# 다이나믹 프로그래밍
import sys
input = sys.stdin.readline

T, W = map(int, input().split())
tree = [0] + list(int(input()) for _ in range(T))
dp = [[0] * (W+1) for _ in range(T+1)]    # dp[i][j] 는 i초 j번 이동

for i in range(1, T+1):
    # j==0 (움직이지 않음, 계속 1번나무)
    if tree[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, W+1):
        # j(움직인 횟수)가 짝수면 1번 나무
        if not j % 2 and tree[i] == 1 or j % 2 and tree[i] == 2:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j])

print(max(dp[-1]))