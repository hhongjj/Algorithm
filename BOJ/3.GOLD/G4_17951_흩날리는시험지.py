# G4 17951 흩날리는 시험지 속에서 내 평점이 느껴진거야
# https://www.acmicpc.net/problem/17951
# 이분탐색

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))

s, e = 0, sum(lst)+1
while s + 1 < e:
    mid = (s + e) // 2
    num, cnt = 0, 0
    for i in range(N):
        num += lst[i]
        if num >= mid:
            cnt += 1
            num = 0
    if cnt >= K:
        s = mid
    else:
        e = mid

print(s)
    