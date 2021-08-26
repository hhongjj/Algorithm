# D2 12711 피자 굽기
from collections import deque

def pizza(start):
    global ans
    stack = [[0, 0] for _ in range(N)]
    i = 0
    idx = 1
    for k in range(N):
        stack[k][0] = ci[idx-1]
        stack[k][1] = idx
        idx += 1
    while 1:
        if stack[i][0]:
            stack[i][0] = stack[i][0] // 2
        if not stack[i][0] and idx != M:
            stack[i][0] = ci[idx-1]
            stack[i][1] = idx
            idx += 1
        i += 1
        if i == N:
            i = 0
        if idx == M:
            cnt = 0
            for j in range(N):
                if stack[j][0]:
                    ans = stack[j][1]
                    cnt += 1
            if cnt == 1:
                break

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    ci = deque(map(int, input().split()))
    ans = 0
    pizza(1)
    print('#{} {}'.format(tc, ans))

