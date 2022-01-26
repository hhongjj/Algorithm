# G4 11559 Puyo Puyo
# https://www.acmicpc.net/problem/11559
# 구현, 그래프 이론, 그래프 탐색, 너비 우선 탐색, 시뮬레이션
# 33% 틀림....
puyo = list(list(input()) for _ in range(12))
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
def del_puyo():
    same_puyo.sort(key=lambda x: (x[0], x[1]), reverse=True)
    while same_puyo:
        x, y = same_puyo.pop()
        if not x:
            puyo[x][y] = '.'
        else:
            puyo[x][y] = '.'
            for i in range(x, 0, -1):
                puyo[i][y] = puyo[i-1][y]

def bfs(alpha, sx, sy):
    global flag, cnt, same_puyo
    q = []
    cont = 1
    temp = []
    temp.append((sx, sy))
    q.append((sx, sy))
    visited[sx][sy] = 1
    while q:
        x, y = q.pop()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6 or visited[nx][ny]:
                continue
            if puyo[nx][ny] == alpha:
                cont += 1
                visited[nx][ny] = 1
                q.append((nx, ny))
                temp.append((nx, ny))

    if cont >= 4:
        same_puyo += temp
        return 1

run, cnt = 1, 0
while run:
    same_puyo = []
    run = 0
    visited = [[0] * 6 for _ in range(12)]
    for i in range(11, -1, -1):
        for j in range(6):
            if puyo[i][j] != '.' and not visited[i][j]:
                result = bfs(puyo[i][j], i, j)
                if result:
                    run = 1
    if run:
        cnt += 1
        del_puyo()

print(cnt)

# ......
# ......
# ......
# ......
# ......
# yyyyyy
# ......
# bbb...
# ......
# c.....
# aaaaaa
#
# puyo = list(list(input()) for _ in range(12))
# dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)
# def del_puyo(same):
#     while same:
#         x, y = same.pop()
#         for i in range(x, 0, -1):
#             puyo[i][y] = puyo[i-1][y]
#         puyo[0][y] = '.'
#
# def bfs(alpha, sx, sy):
#     global flag, cnt
#     q = []
#     cont = 1
#     visited = [[0] * 6 for _ in range(12)]
#     puyo[sx][sy] = '.'
#     q.append((sx, sy))
#     visited[sx][sy] = 1
#     # temp = puyo
#     same_puyo = []
#     while q:
#         x, y = q.pop()
#         for d in range(4):
#             nx, ny = x + dx[d], y + dy[d]
#             if nx < 0 or nx >= 12 or ny < 0 or ny >= 6 or visited[nx][ny]:
#                 continue
#             if puyo[nx][ny] == alpha:
#                 cont += 1
#                 visited[nx][ny] = 1
#                 q.append((nx, ny))
#                 same_puyo.append((nx, ny))
#                 puyo[nx][ny] = '.'
#
#     if cont >= 4:
#         flag = 1
#         cnt += 1
#         del_puyo(same_puyo)
#
# run, cnt = 72, 0
# while run:
#     flag = 0
#     run = 72
#     for i in range(11, -1, -1):
#         for j in range(6):
#             if puyo[i][j] != '.':
#                 bfs(puyo[i][j], i, j)
#             else:
#                 run -= 1
#             if flag:
#                 break
#         if flag:
#             break
#
# print(cnt)