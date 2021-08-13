# 12542 색칠하기

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    color = [list(map(int, input().split())) for _ in range(N)]
    Map = [[0]*10 for _ in range(10)]
    cnt = 0
    for n in range(N):
        for i in range(color[n][0], color[n][2]+1):
            for j in range(color[n][1], color[n][3]+1):
                if Map[i][j] != 0 and Map[i][j] != color[n][4]:
                    Map[i][j] = 3
                    cnt += 1
                else:
                    Map[i][j] = color[n][4]

    print('#{} {}'.format(tc, cnt))