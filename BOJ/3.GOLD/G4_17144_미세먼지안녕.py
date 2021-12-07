# G4 17144 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144
# 구현, 시뮬레이션
import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())
# fine_dust = []
# for r in range(R):
#     temp = list(map(int, input().split()))
#     if temp[0] == -1:
#         air_cleaner = r
#     fine_dust.append(temp)
# air_cleaner -= 1
fine_dust = list(list(map(int, input().split())) for _ in range(R))

# 공기청정기 위치 찾기
for r in range(R):
    if fine_dust[r][0] == -1:
        air_cleaner = r                # 공기 청정기 시작 위치
        break

# 미세먼지 확산
def spread():
    global fine_dust
    visited = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if fine_dust[r][c] and fine_dust[r][c] != -1 and fine_dust[r][c] > 4:
                num = 0
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if nr < 0 or nr >= R or nc < 0 or nc >= C or fine_dust[nr][nc] == -1:
                        continue
                    visited[nr][nc] += fine_dust[r][c] // 5
                    num += 1
                fine_dust[r][c] -= fine_dust[r][c] // 5 * num

    fine_dust = [[c + d for c, d in zip(a, b)] for a, b in zip(fine_dust, visited)]

    return


def move():
    global fine_dust
    x = air_cleaner
    # 공기청정기 윗부분
    # 왼쪽
    for i in range(x, 0, -1):
        fine_dust[i][0] = fine_dust[i-1][0]
    # 위쪽
    for i in range(C-1):
        fine_dust[0][i] = fine_dust[0][i+1]
    # 오른쪽
    for i in range(x):
        fine_dust[i][C-1] = fine_dust[i+1][C-1]
    # 아래쪽
    for i in range(C-1, 1, -1):
        fine_dust[x][i] = fine_dust[x][i - 1]
    fine_dust[x][0] = -1
    fine_dust[x][1] = 0

    # 공기청정기 아랫부분
    # 왼쪽
    for i in range(x+1, R-1):
        fine_dust[i][0] = fine_dust[i+1][0]
    # 아래쪽
    for i in range(C - 1):
        fine_dust[R-1][i] = fine_dust[R-1][i + 1]
    # 오른쪽
    for i in range(R-1, x+1, -1):
        fine_dust[i][C-1] = fine_dust[i-1][C-1]
    # 위쪽
    for i in range(C - 1, 1, -1):
        fine_dust[x+1][i] = fine_dust[x+1][i - 1]
    fine_dust[x+1][0] = -1
    fine_dust[x+1][1] = 0


dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
for _ in range(T):
    spread()
    move()

sum_dust = 0
for r in range(R):
    sum_dust += sum(fine_dust[r])
print(sum_dust+2)
