# S1 13335 트럭
# https://www.acmicpc.net/problem/13335
# 구현, 자료구조, 시뮬레이션, 큐

from collections import deque

n, w, L = map(int, input().split())
a = deque(map(int, input().split()))
cnt, weight = 0, 0
bridge = deque()

while a or bridge:
    cnt += 1
    if bridge:
        if bridge[0][1] + w == cnt:  # 도착시간이면 pop
            weight -= bridge.popleft()[0]
    if a:
        if weight + a[0] <= L:
            weight += a[0]
            bridge.append((a.popleft(), cnt))
            
print(cnt)
        

    