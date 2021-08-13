# S3 2615 오목
# 구현, 브루트포스 알고리즘

import sys 
input = sys.stdin.readline

arr = []
for i in range(19):
    arr.append(list(map(int, input().split())))

visited = [[0]*19 for _ in range(19)]
dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

def go(a,b, cnt):
    for k in range(8):
        x = a + dx[k]
        y = b + dy[k]
        if 0 <= x < 19 and 0 <= y < 19 and arr[x][y] == 1 and visited[x][y] == 0:
            cnt += 1
            visited[x][y] = 1
            go(x, y, cnt)
        elif 0 <= x < 19 and 0 <= y < 19 and arr[x][y] == 2 and visited[x][y] == 0:
            visited[x][y] = 1

    if cnt == 5:
        return cnt


for i in range(19):
    for j in range(19):
        if arr[i][j] == 1:
            a, b = i, j
            visited[a][b] = 1
            cnt = 0
            print(go(a,b, cnt))
            





