# S3 6236 용돈관리

N, M = map(int, input().split())
money = [int(input()) for _ in range(N)]

s, e = max(money), sum(money)

while s <= e:
    mid = (s + e) // 2
    cnt = 0                # 인출 횟수
    sum_m = 0              # 인출 전 까지 총합
    for i in money:
        sum_m += i
        if sum_m > mid:
            cnt += 1
            sum_m = i      # mid 넘기면 이번에 쓴 돈으로 바꿈
    # 인출 다하고 마지막에 돈이 남으면 횟수 더하기
    if sum_m > 0:
        cnt += 1

    # 인출 횟수 초과시 최소 구간 줄임
    if cnt > M:
        s = mid + 1
    # 인출 횟수 만족시 최대 구간 줄임
    else:
        e = mid - 1

print(mid)

# 범위를 정하는 법이 어려웠다. 도움을 받음..
# min을 쓸 돈 중 최대값, max를 쓸 돈 총합으로 둠
# 중간 값을 잡고 쓴 돈이 mid를 넘을 때마다 인출 횟수(cnt) +1해주고
# 마지막에 돈이 남으면 또 +1를 함
# 그리고 인출 횟수랑 M을 비교해서 s,e 값을 조절하면서 구함.