# G5 14719 빗물
# https://www.acmicpc.net/problem/14719
# 구현, 시뮬레이션
#ing

H, W = map(int, input().split())
rain = list(map(int, input().split())) + [0]

if rain.count(0) >= W - 1 or W <= 2:
    print(0)
    exit()

left, right, index = 0, 0, 0
for i, r in enumerate(rain):
    if r > 0:
        left = r
        break

ans = 0
sum_rain, cnt = 0, 0
for w in range(i+1, W):
    if left <= rain[w]:
        ans += cnt*left - sum_rain
        left = rain[w]
        cnt, sum_rain = 0, 0
        continue
    
    if rain[w] > rain[w+1]:
        ans += cnt*rain[w] - sum_rain
        left = rain[w]
        cnt, sum_rain = 0, 0
        continue
    
    cnt += 1
    sum_rain += rain[w]

print(ans)
    
    

        