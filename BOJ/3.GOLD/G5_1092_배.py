# G5 1092 배
# https://www.acmicpc.net/problem/1092
# 그리디 알고리즘, 정렬
from collections import deque

N = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
box = deque(sorted(list(map(int, input().split())), reverse=True))

if crane[0] < box[0]:
    print(-1)
    exit()

i, cnt = 0, 0
while box:
    if not i:
        cnt += 1
        box = deque(sorted(box, reverse=True))
    x = box.popleft()
    if crane[i] >= x:
        i = (i + 1) % N
    else:
        box.append(x)
        if crane[i] < min(box):
            i = 0

print(cnt)
