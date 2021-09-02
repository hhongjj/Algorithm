# S5 19947 투자의 귀재 배주형
# 다이나믹 프로그래밍, 브루트포스 알고리즘, 재귀

import sys
input = sys.stdin.readline

H, Y = map(int,input().split())

year_list = [0] * (Y+1)
year_list[0] = H
for i in range(1, Y+1):
    year_list[i] = int(year_list[i-1] * 1.05)
    if i >= 3:
        year_list[i] = int(max(year_list[i], year_list[i-3] * 1.2))
    if i >= 5:
        year_list[i] = int(max(year_list[i], year_list[i-5] * 1.35))


print(year_list[Y])