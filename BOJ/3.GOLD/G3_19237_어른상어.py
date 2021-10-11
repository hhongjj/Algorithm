# G3 19237 어른 상어
# https://www.acmicpc.net/problem/19237
# 구현, 시뮬레이션


# 상어 이동
def move_shark(n, er, ec, d):
    # # 시간 지남에 따라 냄새 없어짐 계산
    # if shark[er][ec][1] - 1:
    #     shark[er][ec] = (n, shark[er][ec][1] - 1)
    # else:
    #     shark[er][ec] = 0
    # 상어 이동
    idx = 0  # 우선순위
    move = 0  # 빈 곳으로 이동했는지 확인
    for t in range(4):
        l = priority[n-1][d-1][t]
        r, c = er + dr[l-1], ec + dc[l-1]
        if r < 0 or r >= N or c < 0 or c >= N:
            continue
        if shark[r][c] == 0:
            #
            pre[(r, c)] = n
            stack.append((r, c))
            now_shark[n] = (r, c)
            move = 1
            d_list[n-1] = l
            return
        else:
            idx = (idx + 1) % 4
    if move == 0:  # 인근에 빈 곳이 없다면 자기 냄새칸으로 이동.
        # r, c = stack[0]
        shark[er][ec] = (n, 4)
        stack.append((r, c))
        return


def change_smell():
    for s in range(len(stack)-4):
        x, y = stack[s]
        if shark[x][y][1] - 1:
            shark[x][y] = (shark[x][y][0], shark[x][y][1] - 1)
        else:
            shark[x][y] = 0


N, M, K = map(int, input().split())
shark = list(list(map(int, input().split())) for _ in range(N))
d_list = list(map(int, input().split()))
priority = list(list(list(map(int, input().split())) for _ in range(4)) for _ in range(M))
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
now_shark = [0]*(M +1)
stack = [] # 남아있는 냄새 체크
for i in range(N):
    for j in range(N):
        if shark[i][j]:
            now_shark[shark[i][j]] = (i, j)
            shark[i][j] = (shark[i][j], 4)
            stack.append((i, j))
print(shark)
print(now_shark)
sec = 0
while sec < 15:
    pre = {}
    for n in range(len(now_shark)-1, 0, -1):
        d = d_list[n-1]
        nr, nc = now_shark[n]
        move_shark(n, nr, nc, d)
        sec += 1
    print(pre)
    for p in pre:
        r, c = p
        shark[r][c] = (n, 4)
    change_smell()
print(shark)