# S1 9764 서로 다른 자연수의 합 https://www.acmicpc.net/problem/9764
# 다이나믹 프로그래밍
# 실패 잘 모르겠음...


import sys
sys.setrecursionlimit(10**7)

def sol(num, use):
    if not num:
        return 1
    if num < 0 or num < use:
        return 0
    dp[num][use] = (sol(num - use, use + 1) % mod + sol(num, use + 1) % mod) % mod
    if dp[num][use] != -1:
        return
    ref = dp[num][use]
    return ref


mod = 100999
T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[-1]*(N+1) for _ in range(N+1)]
    res = sol(N, 1)
    print(res)





# dp[n][m] n까지의 서로 다른 자연수(m)를 사용해서 n을 만들 수 있는 가지 수
#  dp[n][j]= dp[n-j][j+1]+dp[n][j+1] j를 사용한 경우와 사용하지 않은 경우


