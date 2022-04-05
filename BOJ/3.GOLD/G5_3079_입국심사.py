# G5 3079 입국심사
# https://www.acmicpc.net/problem/3079
# 이분 탐색, 매개 변수 탐색
# 아직 ing

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Tk = list(int(input()) for _ in range(N))

s, e = 0, max(Tk) * M
while s <= e:
    mid = (s + e) // 2
    cnt = 0
    for i in range(N):
        pass

