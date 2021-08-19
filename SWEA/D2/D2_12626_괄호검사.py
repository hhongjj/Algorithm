# D2 12626 괄호검사

T = int(input())

for tc in range(1, T+1):
    lst = input()
    stack = []
    print('#{}'.format(tc), end=' ')
    check = 0
    for i in lst:
        if i == '(' or i == '{':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                check = 1
                break
        elif i == '}':
            if len(stack) != 0 and stack[-1] == '{':
                stack.pop()
            else:
                check = 1
                break
    if not check and len(stack) == 0:
        print(1)
    else:
        print(0)


# 처음에 stack이 비어있을 때의 경우를 생각하지 못해서 런타임에러 떴었다.
# 예외처리 하는 부분이 중요!