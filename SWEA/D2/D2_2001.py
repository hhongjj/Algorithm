#2001 파리 퇴치

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    score = 0
    for i in range(N-M):
        for j in range(N-M):
            sum_score = 0
            for k in range(M):
                sum_score += arr[i+k][j+k]
            if score < sum_score:
                score = sum_score
    print('#{} {}'.format(tc, score))


