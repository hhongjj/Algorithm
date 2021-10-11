# G3 19237 어른 상어
# https://www.acmicpc.net/problem/19237
# 구현, 시뮬레이션
# 아직

# 상어 이동
def move_shark():
    pre = {}
    past = now_shark[:]
    move = [0] * 5  # 빈 곳으로 이동했는지 확인
    delete_shark = []
    # 어디로 이동하는 지
    for n in range(len(now_shark)-1, 0, -1):
        d = d_list[n-1]
        er, ec = now_shark[n]
        idx = 0  # 우선순위
        for t in range(4):
            l = priority[n-1][d-1][t]
            nr, nc = er + dr[l-1], ec + dc[l-1]
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if shark[nr][nc] == 0:
                if (nr, nc) in pre.keys():                  # 만약에 같은 곳으로 이동하는 상어 있으면 4부터 돌고 있으므로 삭제할 것이기 때문에 그전에 상어의 번호를 저장.
                    delete_shark.append(pre[(nr, nc)])
                pre[(nr, nc)] = n  # 움직일 방향 저장 -> 같은 곳에 가면 쫓겨나므로 일단 pre 에 저장
                move[n] = 1
                break
            else:
                idx = (idx + 1) % 4
    # 이전에 냄새들 하나씩 뺴줌
    change_smell()
    # 이동시킴
    for p, n in pre.items():
        r, c = p
        shark[r][c] = (n, 4)
        now_shark[n] = (r, c)
        stack.append((r, c))
    # 이동하면서 삭제될 상어 now_shark 에서 삭제. 상어번호가 큰거부터 삭제해야하므로 정렬해줌.
    delete_shark.sort(reverse=True)
    for k in range(len(delete_shark)):
        del now_shark[delete_shark[k]]

    if sum(move) != len(now_shark)-1:  # 인근에 빈 곳이 없다면 자기 냄새칸으로 이동.
        for m in range(1, len(now_shark)):
            if move[m] == 0:
                r, c = past[m]
                shark[r][c] = (n, 4)
                stack.append((r, c))
                now_shark[m] = (r, c)
    return


def change_smell():
    delete = []
    for s in range(len(stack)):
        x, y = stack[s]
        if shark[x][y][1] - 1:
            shark[x][y] = (shark[x][y][0], shark[x][y][1] - 1)
        else:
            shark[x][y] = 0
            delete.append(s)
    for k in range(len(delete)-1, -1, -1):
        del stack[delete[k]]
    return

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
#[[0, 0, 0, 0, (3, 4)], [0, (2, 4), 0, 0, 0], [(1, 4), 0, 0, 0, (4, 4)], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# [0, (2, 0), (1, 1), (0, 4), (2, 4)]

sec = 1
while sec < 15:
    move_shark()
    print(sec, shark)
    print(now_shark)
    sec += 1




# # 상어 이동
# def move_shark(n, er, ec, d):
#     # # 시간 지남에 따라 냄새 없어짐 계산
#     # if shark[er][ec][1] - 1:
#     #     shark[er][ec] = (n, shark[er][ec][1] - 1)
#     # else:
#     #     shark[er][ec] = 0
#     # 상어 이동
#     idx = 0  # 우선순위
#     move = 0  # 빈 곳으로 이동했는지 확인
#     for t in range(4):
#         l = priority[n-1][d-1][t]
#         r, c = er + dr[l-1], ec + dc[l-1]
#         if r < 0 or r >= N or c < 0 or c >= N:
#             continue
#         if shark[r][c] == 0:
#             #
#             pre[(r, c)] = n
#             stack.append((r, c))
#
#             move = 1
#             d_list[n-1] = l
#             return
#         else:
#             idx = (idx + 1) % 4
#     if move == 0:  # 인근에 빈 곳이 없다면 자기 냄새칸으로 이동.
#         # r, c = stack[0]
#         shark[er][ec] = (n, 4)
#         stack.append((r, c))
#         return
#
#
# def change_smell():
#     for s in range(len(stack)-4):
#         x, y = stack[s]
#         if shark[x][y][1] - 1:
#             shark[x][y] = (shark[x][y][0], shark[x][y][1] - 1)
#         else:
#             shark[x][y] = 0
#
#
# N, M, K = map(int, input().split())
# shark = list(list(map(int, input().split())) for _ in range(N))
# d_list = list(map(int, input().split()))
# priority = list(list(list(map(int, input().split())) for _ in range(4)) for _ in range(M))
# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]
# now_shark = [0]*(M +1)
# stack = [] # 남아있는 냄새 체크
# for i in range(N):
#     for j in range(N):
#         if shark[i][j]:
#             now_shark[shark[i][j]] = (i, j)
#             shark[i][j] = (shark[i][j], 4)
#             stack.append((i, j))
# print(shark)
# print(now_shark)
# sec = 0
# while sec < 15:
#     pre = {}
#     for n in range(len(now_shark)-1, 0, -1):
#         d = d_list[n-1]
#         nr, nc = now_shark[n]
#         move_shark(n, nr, nc, d)
#         sec += 1
#     for p in pre:
#         r, c = p
#         shark[r][c] = (n, 4)
#         now_shark[n] = (r, c)
#     change_smell()
#     print(shark)