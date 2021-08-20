# S3 14327 파닭파닭
# 이분 탐색

import sys
input = sys.stdin.readline
S, C = map(int, input().split())

pa = [int(input()) for _ in range(S)]

s, e = 1, max(pa)
while s <= e:
    cnt = 0
    mid = (s + e) // 2
    tmp = pa[:]
    for i in range(S):
        cnt += pa[i] // mid
    if cnt < C:
        e = mid - 1
    else:
        s = mid + 1

sum_la = sum(pa) - e*C
print(sum_la)

# s는 1, e는 제일 긴 파를 선택
# 파를 mid로 나눈 몫을 cnt에 더함
# cnt가 C보다 작으면 e를 -1 해주면서 계산함
# mid 대신 e를 해야함. cnt가 C를 만족하면서 파의 길이가 최대값이여야 함으로
# for i in range(S):
#         cnt += pa[i] // mid
#         tmp[i] -= mid* (pa[i]//mid)
#     if cnt == C and min(tmp) == 0:
#         break
# 이렇게도 해봤는데 시간초과뜸.



