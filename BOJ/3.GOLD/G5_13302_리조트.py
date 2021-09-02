# G5 13302 리조트
# 다이나믹 프로그래밍
# 쿠폰 방법을 모르겠다..

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
KOI = [0]*(N+1)
res = [[0]*(N+1) for _ in range(N+1)]
lst = list(map(int, input().split()))
for i in lst:
    KOI[i] = 1

coupon = 0
for i in range(1, N+1):
    if not KOI[i]:
        res[i] = res[i-1]+10000
    else:
        res[i] = res[i-1]
    if i >= 3:
        if res[i] >= res[i-3]+25000 or coupon+1 :
            res[i] = res[i-3]+25000
            coupon += 1
        # res[i] = min(res[i], res[i-3]+25000)
        # coupon += 1
    if i >= 5:
        if res[i] >= res[i-5]+37000:
            res[i] = res[i-5]+37000
            coupon += 2




print(res)
print(coupon)

# [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0]