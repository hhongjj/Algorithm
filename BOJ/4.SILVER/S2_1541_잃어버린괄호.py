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
# 연산자를 기준으로 연산자와 함께 stack에 넣는다.  deque(['55', '-50', '+40'])

result = int(stack.popleft())
minus = 0
while stack:
    num = stack.popleft()
    if num[0] == '-':                  # 만약 -라면 그다음 -가 나올때 까지 숫자를 다 minus에 더한다.
        minus += int(num[1:])
        while stack:
            num = stack.popleft()
            if num[0] == '+':
                minus += int(num[1:])
            else:                     # - 가 나오면 다시 stack에 넣어 준다.
                stack.appendleft(num)
                break
    else:                             # -가 바로 앞에 없다면 그냥 result에 더해준다.
        result += int(num[1:])

# result값과 minus 값을 빼준다.
print(result-minus)
