# G4 1477 휴게소 세우기
# https://www.acmicpc.net/problem/1477
# 이분 탐색, 매개 변수 탐색
# 미완성
import sys
input = sys.stdin.readline

N, M, L = map(int, input().split())
rest = list(map(int, input().split())) + [0, L]
rest.sort()
start, end = 0, L - 1

while start <= end:
    mid = (start + end) // 2
    # if mid == 0 or mid == 1:
    #     mid = 1
    #     start = mid
    #     break
    cnt = 0
    for i in range(1, len(rest)):
        if (rest[i] - rest[i-1]) > mid:
            cnt += (rest[i] - rest[i-1] - 1) // mid

    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        # ans = mid

print(start)
# print(ans)

# import heapq as hq
# 
# n, m, l = map(int, input().split())
# facility = sorted(list(map(int, input().split())))
# 
# # 각 휴게소 사이의 거리를 최대힙 구조로 담는다.
# # 거리를 큐에 담을 때는 등분한 횟수를 같이 입력하고, 초기값은 1이다.
# distance = []
# for i in range(len(facility)):
#     if i == 0:  # 시작점~첫번째 휴게소 사이 거리
#         hq.heappush(distance, (-facility[i], 1))
#     else:
#         hq.heappush(distance, (-(facility[i] - facility[i - 1]), 1))
#     if i == len(facility) - 1:  # 마지막 휴게소~끝점 사이 거리
#         hq.heappush(distance, (-(l - facility[-1]), 1))
# 
# # 가장 긴 구간을 k등분해나간다.
# for _ in range(m):
#     longest, divided = hq.heappop(distance)
#     # 등분하기 전 원래 거리값을 k등분으로 해줘야 한다.
#     longest = -longest * divided
#     hq.heappush(distance, ((-longest / (divided + 1)), divided + 1))
# 
# answer = -hq.heappop(distance)[0]
# if answer == int(answer):
#     print(int(answer))
# else:
#     print(int(answer) + 1)