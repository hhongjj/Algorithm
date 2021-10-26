# G2 3109 빵집
# https://www.acmicpc.net/problem/3109
# 그래프 이론, 그리디 알고리즘, 그래프 탐색, 깊이 우선 탐색
import sys
input = sys.stdin.readline


def dfs(r, c):
    global flag
    lst[r][c] = 1     # 방문 했으므로 1로 바꿔 준다.
    if c == C - 1:    # 마지막 열에 도착했으면 flag True로 바꿔주고 return
        flag = True
        return
    for d in range(3):
        nr, nc = r + dr[d], c + 1
        if nr < 0 or nr >= R or nc >= C or lst[nr][nc] == 1 or lst[nr][nc] == 'x':    # 범위를 벗어나거나 방문했거나 벽('x')일 경우 continue
            continue
        dfs(nr, nc)       # 위의 경우가 아니면 재귀
        if flag:          # 마지막 열에 도착했으면 return
            return


R, C = map(int, input().split())
lst = list(list(input().rstrip()) for _ in range(R))
dr = (-1, 0, 1)

cnt = 0
for i in range(R):
    flag = False  # 마지막 열에 도착했는지 확인
    dfs(i, 0)     # 0 열의 모든 점이 출발점
    if flag:      # 마지막 열에 도착했으므로 cnt +1 해준다.
        cnt += 1
print(cnt)
