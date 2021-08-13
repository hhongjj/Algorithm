# D2 12579 앞글자따기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sen = input().split()
    word = ''
    for i in range(N):
        word += sen[i][0].upper()
    print('#{} {}'.format(tc, word))