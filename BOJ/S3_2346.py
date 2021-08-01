# 2346 풍선 터뜨리기
# 자료구조, 덱

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

deq = deque([(idx+1, i) for idx, i in enumerate(num)])

ans = []
for i in range(N):
    bal = deq.popleft()
    ans.append(bal[0])
    if bal[1] > 0:                                     # num 양수이면 시계 반대방향
        deq.rotate(-(bal[1] - 1))                      # rotate는 -이여야 시계 반대방향임.
    else:
        deq.rotate(-bal[1])

print(*ans)

# rotate(n) 함수를 통해 deque를 회전시킴.
# n이 양수일 때 : 시계 방향으로 n칸 만큼 회전
# n이 음수일 때 : 반시계 방향으로 n칸 만큼 회전
