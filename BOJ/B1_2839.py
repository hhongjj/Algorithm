# 2839 설탕 배달
# 수학, 다이나믹 프로그래밍, 그리디 알고리즘, 브루트포스 알고리즘

import sys 
input = sys.stdin.readline

N = int(input())

while 1:
    cnt = 0
    if N % 5 == 0:
        print(N // 5)
        break
    elif (N % 5) % 3 == 0:
        cnt += N // 5
        cnt += (N % 5) // 3
        print(cnt)
        break
    elif (N % 3) % 5 == 0:
        cnt += N // 3
        cnt += (N % 3) // 5
        print(cnt)
        break
    else:
        print(-1)
        break








