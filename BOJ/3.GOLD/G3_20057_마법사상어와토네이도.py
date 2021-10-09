# G3 20057 마법사 상어와 토네이도
# https://www.acmicpc.net/problem/20057
# 구현, 시뮬레이션

# 좌표 이동 방향 찾기
def find_out_direction(er, ec):
    if er == ec and er <= N // 2:              # 왼쪽 위 대각선 -> 좌
        return er, ec - 1, 0
    elif er == ec and er > N // 2:             # 오른쪽 아래 대각선 -> 상
        return er - 1, ec, 3
    elif er + ec + 1 == N:
        if er > N // 2:                        # 왼쪽 아래 대각선 -> 우
            return er, ec + 1, 2
        else:                                  # 오른쪽 위 대각선 -> 좌
            return er, ec - 1, 0
    elif er < ec:
        if er + ec < N - 1:                    # 위쪽 부분 대각선 사이 -> 좌
            return er, ec - 1, 0
        else:                                  # 오른쪽 부분 대각선 사이 -> 상
            return er - 1, ec, 3
    elif er > ec:
        if er + ec < N - 1:                    # 왼쪽 부분 대각선 사이 -> 하
            return er + 1, ec, 1
        else:                                  # 아래쪽 부분 대각선 사이 -> 우
            return er, ec + 1, 2


# 그걸 토대로 모래 비율 방향도 바꿔 옮기기
def move_sand(er, ec, d):
    # 방향에 따른 모래 비율 (0:좌, 1:하, 2:우, 3:상)
    d_list = [[[0, 0, 2, 0, 0], [0, 10, 7, 1, 0], [5, 'a', 0, 0, 0], [0, 10, 7, 1, 0], [0, 0, 2, 0, 0]],
              [[0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [2, 7, 0, 7, 2], [0, 10, 'a', 10, 0], [0, 0, 5, 0, 0]],
              [[0, 0, 2, 0, 0], [0, 1, 7, 10, 0], [0, 0, 0, 'a', 5], [0, 1, 7, 10, 0], [0, 0, 2, 0, 0]],
              [[0, 0, 5, 0, 0], [0, 10, 'a', 10, 0], [2, 7, 0, 7, 2], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]]
    




#     now = sand[er][ec]
#     lst = [((er-2, ec), 0.02), ((er-1, ec-1), 0.1), ((er-1, ec), 0.07), ((er-2, ec), 0.01),
#            ((er, ec-2), 0.05), ((er+1, ec-1), 0.1), ((er+1, ec), 0.07), ((er+1, ec+1), 0.01), ((er+2, ec), 0.02),]
#     move_sum = 0
#     if d == 0:    # 좌
#         for i in range(len(lst)):
#             sand[lst[i][0][0]][lst[i][0][1]] += int(now*lst[i][1])
#             move_sum += int(now*lst[i][1])
#     elif d == 1:  # 하
#         for i in range(len(lst)):
#             r, c = er + dr[d], ec + dc[d]
#             sand[r][c] += int(now*lst[i][1])
#             move_sum += int(now*lst[i][1])
# # ... 규칙이 있지 않을까? 설마 하나씩 다해야하나 할 수는 있긴한데..rotate 하는거 찾아보자








N = int(input())
sand = list(list(map(int, input().split())) for _ in range(N))
nr, nc = N//2, N//2  # 시작 지점은 항상 정중앙
dr = [0, 1, 0, -1]  # 방향만 (0:좌, 1:하, 2:우, 3:상)
dc = [-1, 0, 1, 0]
# while nr == 1 and nc ==1:
#     pass
# nr, nc, d = find_out_direction(nr, nc)   # 옮겨진 좌표와 방향
# move_sand(nr, nc, d)


# sand[er-2][ec] += int(now*0.02)
# sand[er-1][ec-1] += int(now*0.1)
# sand[er-1][ec] += int(now*0.07)
# sand[er][ec+1] += int(now*0.01)
# sand[er][ec-2] += int(now*0.05)
# sand[er+1][ec-1] += int(now*0.1)
# sand[er+1][ec] += int(now*0.07)
# sand[er+1][ec+1] += int(now*0.01)
# sand[er+2][ec] += int(now*0.02)