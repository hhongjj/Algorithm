# G3 10800 컬러볼
# https://www.acmicpc.net/problem/10800
# 구현, 정렬, 누적 합
# 시간 초과..
import copy
import sys
input = sys.stdin.readline

N = int(input())
ball, color = [], {}
for i in range(N):
    c, s = map(int, input().split())
    ball.append([i, c, s])
    if c in color:
        temp = color[c]
        color[c] = temp + [s]
    else:
        color[c] = [s]

ball_sorted = copy.deepcopy(ball)   # sorted 인데 왜 바뀔까?
ball_temp = sorted(ball, key=lambda x: x[2])
ball_sorted.sort(key=lambda x: x[2])

t = 0
for i in range(1, N):
    if ball_temp[i][2] != ball_temp[i - 1][2]:
        ball_sorted[i][2] += ball_sorted[i-1][2] + t
        t = 0
    elif ball_temp[i][2] == ball_temp[i-1][2]:
        t += ball_temp[i][2]
        ball_sorted[i][2] = ball_sorted[i-1][2]

ball_sorted.sort(key=lambda x: x[0])
for i in color.keys():
    temp = color[i]
    temp.sort()
    color[i] = temp

for x, y, z in ball_sorted:
    temp = color[y]
    index = temp.index(ball[x][2])
    sub_sum = sum(temp[:index+1])
    print(z-sub_sum)


# 5
# 3 15
# 3 15
# 3 5
# 1 15
# 2 10
# 10
# 10
# 0
# 15
# 5