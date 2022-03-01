# S1 21758  꿀 따기
# https://www.acmicpc.net/problem/21758
# 그리디 알고리즘, 누적 합, 많은 조건 분기

import sys
input = sys.stdin.readline

N = int(input())
honey = list(map(int, input().split()))

# 꿀통-벌벌
total = sum(honey) - honey[-1]
two = honey[0]
ans = 0
for i in range(1, N-1):
    ans = max(ans, total - honey[i] + two)
    two += honey[i]

# 벌-벌-꿀통
total = sum(honey) - honey[0]
two = honey[-1]
for i in range(N-2, 0, -1):
    ans = max(ans, total-honey[i] + two)
    two += honey[i]

# 벌-꿀통-벌
total = sum(honey)
for i in range(1, N-1):
    ans = max(ans, total-honey[0]-honey[-1] + honey[i])

print(ans)
