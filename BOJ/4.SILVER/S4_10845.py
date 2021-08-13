# 10845 큐
# 18258 큐 2는 deque 썼어야했음.

import sys 
input = sys.stdin.readline

N = int(input())
que = []
for i in range(N):
    word = input().split()
    if word[0] == 'push':
        que.append(word[1])
    elif word[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
            del que[0]
    elif word[0] == 'size':
        print(len(que))
    elif word[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif word[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    else:
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
