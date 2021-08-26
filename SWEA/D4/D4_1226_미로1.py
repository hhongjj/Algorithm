# D4 1226 미로1

from collections import deque

dy = [-1,1,0,0]
dx = [0,0,-1,1]

def bfs(sy, sx):
    queue = deque()
    queue.append((sy, sx))
    MAP[sy][sx] = 1

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= 16 or nx >= 16 : continue
            if MAP[ny][nx] == 1: continue    # 벽과 방문했던 곳
            if MAP[ny][nx] == 3:             # 도착점 도달
                return 1
            MAP[ny][nx] = 1                  # 방문 표시
            queue.append((ny, nx))
    return 0         # 도착점에 도달 못 함 

for _ in range(10):
    tc = int(input())
    MAP = [list(map(int, input())) for _ in range(16)]
    flag = 0
    # 출발점 구하기
    for y in range(16):
        for x in range(16):
            if MAP[y][x] == 2:
                sy, sx = y, x
                flag = 1
                break
        if flag:
            break
    res = bfs(sy, sx)
    print('#{} {}'.format(tc, res))