# 2839 설탕 배달
# 수학, 다이나믹 프로그래밍, 그리디 알고리즘, 브루트포스 알고리즘

import sys 
input = sys.stdin.readline

N = int(input())

cnt = 0
while 1:
    # if N < 3:
    #     print(-1)
    #     break
    if N >= 5:
        N -= 5
        cnt += 1
    elif N >= 3:
        N -= 3
        cnt += 1
    elif N == 0:
        print(cnt)
        break
    else:
        print(-1)
        break

# print(cnt)