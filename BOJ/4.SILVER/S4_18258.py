# 18258_큐 2
# 자료구조, 큐

from collections import deque
import sys 
input = sys.stdin.readline

N = int(input())
que = deque()
for i in range(N):
    word = input().split()
    if word[0] == 'push':
        que.append(word[1])
    elif word[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())
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


# 처음엔 함수로 구현을 해야하나 고민함
# push일 때 맨 앞에 넣어야 하는 줄 알았음.
# 시간 초과 뜸. -> 덱 씀
# 10845 큐는 이렇게 했으면 가능.
# import sys 
# input = sys.stdin.readline

# N = int(input())
# que = []
# for i in range(N):
#     word = input().split()
#     if word[0] == 'push':
#         que.append(word[1])
#     elif word[0] == 'pop':
#         if len(que) == 0:
#             print(-1)
#         else:
#             print(que[0])
#             del que[0]
#     elif word[0] == 'size':
#         print(len(que))
#     elif word[0] == 'empty':
#         if len(que) == 0:
#             print(1)
#         else:
#             print(0)
#     elif word[0] == 'front':
#         if len(que) == 0:
#             print(-1)
#         else:
#             print(que[0])
#     else:
#         if len(que) == 0:
#             print(-1)
#         else:
#             print(que[-1])