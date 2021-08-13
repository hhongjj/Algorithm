#1021 회전하는 큐
#자료구조 덱

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
deq = deque([i for i in range(1,N+1)])
num = deque(list(map(int,input().split())))

cnt = 0
while num:
    if deq[0] == num[0]:
        deq.popleft()
        num.popleft()
    elif len(deq)//2 >= deq.index(num[0]):
        cnt += deq.index(num[0])
        deq.rotate(-deq.index(num[0]))
    else:
        cnt += len(deq)-deq.index(num[0])
        deq.rotate(len(deq)-deq.index(num[0]))

print(cnt)


# 뽑아내려는 원소의 위치가 deq의 중간 앞에 있다면 앞의 숫자들 다 뒤로 보냄.
# 뽑아내려는 원소의 위치가 deq의 중간 뒤에 있다면 전체 길이에서 뺀다음 
# 뽑아내려는 원소를 포함해서 뒷부분 전체다 앞으로 오게함.