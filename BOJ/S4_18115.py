# 18115 카드 놓기
# 자료 구조, 덱

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

deq  = deque([i for i in range(1,N+1)])

ans = deque()

for i in range(len(A)-1, -1, -1):
    if A[i] == 1:
        ans.appendleft(deq.popleft())
    elif A[i] == 2:
        first = ans.popleft()
        ans.appendleft(deq.popleft())
        ans.appendleft(first)
    else:
        ans.append(deq.popleft())

print(*ans)                     # for문 쓰지 않고 list 다 출력.


