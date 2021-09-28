# S2 1541 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
# 수학, 문자열, 그리디 알고리즘, 피싱
from collections import deque

lst = input()
stack = deque()
for i in lst:
    if i.isdigit():
        if stack:
            tmp = stack.pop() + i
            stack.append(tmp)
        else:
            stack.append(i)
    else:
        stack.append(i)
result = int(stack.popleft())
minus = 0
while stack:
    num = stack.popleft()
    if num[0] == '-':
        minus += int(num[1:])
        while stack:
            num = stack.popleft()
            if num[0] == '+':
                minus += int(num[1:])
            else:
                stack.appendleft(num)
                break
    else:
        result += int(num[1:])

print(result-minus)



