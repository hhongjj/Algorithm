# 2667 단지번호붙이기
#
import sys
input = sys.stdin.readline

N = int(input())
home = []
for i in range(N):
    home.append(list(map(int,input().rstrip())))

visit = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
new = []
for i in range(N):
    for j in range(N):
        if not home[i][j] or visit[i][j]:
            continue
        count = 1
        stack = [[i, j]]
        visit[i][j] = 1
        while stack:
            p, q = stack.pop()

            for k in range(4):
                x = p + dx[k]
                y = q + dy[k]
                if 0 <= x < N and 0 <= y < N and home[x][y] and not visit[x][y]:
                    stack.append([x,y])
                    count += 1
                    visit[x][y] = 1

        new.append(count)
        cnt += 1

print(cnt)
new = sorted(new)
for i in new:
    print(i)