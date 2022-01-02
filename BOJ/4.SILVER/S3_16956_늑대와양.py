# S3 16956 늑대와 양
# https://www.acmicpc.net/problem/16956
# 그래프 이론, 그래프 탐색, 애드 혹, 구성적

R, C = map(int, input().split())
farm = list(list(input()) for _ in range(R))

wolf = []
for i in range(R):
    for j in range(C):
        if farm[i][j] == 'W':
            wolf.append((i, j))

dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
flag = 1
while wolf:
    r, c = wolf.pop()
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or farm[nr][nc] == 'W':
            continue
        if farm[nr][nc] == 'S':
            flag = 0
            break
        farm[nr][nc] = 'D'

if flag:
   print(flag)
   for i in range(R):
       print(''.join(farm[i]))
else:
    print(flag)

# 늑대 주위를 다 울타리를 치고 만약에 바로 주위에 양이 있다면 그대로 break
