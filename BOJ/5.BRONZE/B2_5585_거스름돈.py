# 5585 거스름돈
# 그리디 알고리즘

import sys
input = sys.stdin.readline

money = 1000 - int(input())

cnt = 0
while money != 0:
    if money >= 500:
        cnt += 1
        money -= 500
    elif money >= 100:
        cnt += 1
        money -= 100
    elif money >= 50:
        cnt += 1
        money -= 50
    elif money >= 10:
        cnt += 1
        money -= 10
    elif money >= 5:
        cnt += 1
        money -= 5
    else:
        cnt += 1
        money -= 1

print(cnt)



