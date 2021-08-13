# 4796 캠핑
# 수학, 그리디 알고리즘

import sys
input = sys.stdin.readline

idx = 0
while 1:
    sum = 0
    L, P, V = map(int,input().split())
    if L == 0:
        break
    sum += (V // P) * L
    if (V % P) > L:
        sum += L
    else:
        sum += (V % P)
    idx += 1
    print(f'Case {idx}: {sum}')


# V일 짜리 휴가를 연속하는 P일로 나누고 몫을 L일과 곱함
# 그리고남는 일이 L보다 크면 L만 더하고 아니면 나머지를 더함