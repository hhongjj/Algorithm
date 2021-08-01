# 2164 카드2
# 자료구조, 큐

import sys
from collections import deque

input = sys.stdin.readline

deq  = deque()

N = int(input())
for i in range(1,N+1):
    deq.append(i)

while len(deq) > 1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq.popleft())



# queue 가 deque 보다 느림!!
#import sys
# from queue import Queue

# input = sys.stdin.readline

# que = Queue()

# N = int(input())
# for i in range(1,N+1):
#     que.put(i)

# while que.qsize() > 1:
#     que.get()
#     data = que.get()
#     que.put(data)


# print(que.get())