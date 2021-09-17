# G4 9935 문자열폭발
# https://www.acmicpc.net/problem/9935
# 자료구조, 문자열, 스택
# 시간 초과...

import sys
from collections import deque
input = sys.stdin.readline

lst = input().rstrip()
bomb = input().rstrip()

while bomb in lst:
    stack = deque()
    i = 0
    while i < len(lst):
        if lst[i] == bomb[0]:
            run = 1
            j = i
            for b in range(len(bomb)):
                if lst[j] != bomb[b]:
                    run = 0
                    break
                j += 1
            if run:
                stack.append(i)
                i += len(bomb)
            else:
                i += 1
        else:
            i += 1
    lst = list(lst)
    while stack:
        idx = stack.pop()
        for b in range(len(bomb)-1, -1, -1):
            lst.pop(idx+b)
    lst = ''.join(lst)

if len(lst):
    print(lst)
else:
    print('FRULA')

# 시간 초과
# import sys
# input = sys.stdin.readline
#
# lst = input().rstrip()
# bomb = input().rstrip()
#
# while bomb in lst:
#     lst = lst.replace(bomb, "")
#
# if len(lst):
#     print(lst)
# else:
#     print('FRULA')
