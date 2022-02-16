# B3 10250 ACM 호텔
# https://www.acmicpc.net/problem/10250
# 수학, 구현, 사칙연산

T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    YY = n % h
    if n % h:
        roomnum = str(n % h)
        if len(str(n//h + 1)) == 1:
            roomnum += '0' + str(n//h + 1)
        else:
            roomnum += str(n//h + 1)
    else:
        roomnum = str(h)
        if len(str(n//h)) == 1:
            roomnum += '0' + str(n//h)
        else:
            roomnum += str(n//h)

    print(roomnum)