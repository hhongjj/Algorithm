#10866 덱

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
deq = deque()
for i in range(N):
    word = input().split()
    if word[0] == 'push_front':
        deq.appendleft(int(word[1]))
    elif word[0] == 'push_back':
        deq.append(int(word[1]))
    elif word[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif word[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop()) 
    elif word[0] == 'size':
        print(len(deq))
    elif word[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0) 
    elif word[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0]) 
    else:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1]) 
