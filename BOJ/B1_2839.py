# 2839 설탕 배달
# 수학, 다이나믹 프로그래밍, 그리디 알고리즘, 브루트포스 알고리즘

import sys 
input = sys.stdin.readline

N = int(input())
run = 1
min_cnt = 0
while run:
    if N % 5 == 0:
        print(N // 5)
        break
    elif (N % 5) % 3 == 0:
        print (N // 5 + (N % 5) // 3)
        break
    else:
        cnt = N // 5
        for i in range(cnt-1,0,-1):
            if (N - (5*i)) % 3 == 0:
                min_cnt = i+ ((N-(5*i))//3)
                run = 0
                break
        if run == 1:
            min_cnt = -1
            break
    if N % 3 == 0:
        if min_cnt > N // 3:
            min_cnt = N // 3
            print(min_cnt)
            break
        else:
            print(min_cnt)
            break
    else:
        print(min_cnt)
        break