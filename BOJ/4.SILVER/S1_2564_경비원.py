# S1 2564 경비원
# https://www.acmicpc.net/problem/2564
# 구현, 많은 조건 분기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = int(input())
store = list(map(int, input().split()) for _ in range(s))
x, y = map(int, input().split())

ans = 0
for i, j in store:
    if i == x:
        ans += abs(y - j)
    else:
        if i == 1:
            if x == 2:
                ans += min((y+m+j), (n-y+m+n-j))
            elif x == 3:
                ans += j + y
            else:
                ans += n-j + y
        elif i == 2:
            if x == 1:
                ans += min((y+m+j), (n-y+m+n-j))
            elif x == 3:
                ans += j + m - y
            else:
                ans += n - j + m - y
        elif i == 3:
            if x == 1:
                ans += j + y
            elif x == 2:
                ans += m-j + y
            else:
                ans += min((j+n+y),(m-j+n+m-y))
        else:
            if x == 1:
                ans += n - j + y
            elif x == 2:
                ans += n - j + m - y
            else:
                ans += min((j+n+y),(m-j+n+m-y))
print(ans)
                
