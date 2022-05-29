# G4 16120 PPAP
# https://www.acmicpc.net/problem/16120
# 자료 구조, 그리디 알고리즘, 스택
import sys
input = sys.stdin.readline

lst = input().rstrip()

stack = []
ppap = ['P','P','A','P']
if lst == ppap or lst == ['P']:
    print('PPAP')
else:
    for i in lst:
        stack.append(i)
        if stack[-4:] == ppap:
            stack.pop()
            stack.pop()
            stack.pop()

if stack == ppap or stack == ['P']:
    print('PPAP')
else:
    print('NP')

# 시간초과
# while lst.find('PPAP')>=0:
#     cnt = lst.count('PPAP')
#     lst = lst.replace('PPAP', 'P', cnt)
# if lst=='P':
#     print('PPAP')
# else:
#     print('NP')