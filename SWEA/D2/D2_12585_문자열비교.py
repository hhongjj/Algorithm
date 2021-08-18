# D2 12585 문자열 비교

T = int(input())

for tc in range(1, T+1):
    N = list(input())
    M = list(input())
    cnt = 0
    idx = 0
    for i in range(len(M)):
        if N[idx] == M[i]:
            cnt += 1
            idx += 1
        else:
            cnt = 0
            idx = 0
        if cnt == len(N):
            print('#{} {}'.format(tc, 1))
            break
    if cnt != len(N):
        print('#{} {}'.format(tc, 0))

