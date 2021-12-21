# G4 1477 휴게소 세우기
# https://www.acmicpc.net/problem/1477
# 이분 탐색, 매개 변수 탐색

import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
rest = list(map(int, input().split())) + [0, L-1]
rest.sort()
start, end = 1, L-1

while start <= end:
    mid = (start + end) // 2
    if mid == 0:
        mid = 1
    cnt = 0
    for i in range(1, len(rest)):
        if (rest[i] - rest[i-1]) > mid:
            cnt += (rest[i] - rest[i-1]) // mid
            if (rest[i] - rest[i-1]) % mid == 0:
                cnt -= 1
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        result = mid
# print(result)
print(start)