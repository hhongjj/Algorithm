# D4 1224 계산기3

def postfix(lst, N):
    i = 0
    stack = []
    while i < N:
        if ord('0') <= ord(lst[i]) <= ord('9'):
            res.append(lst[i])
        else:
            if lst[i] == '(':
                stack.append(lst[i])
            if lst[i] == '+':
                while stack and (stack[-1] == '+' or stack[-1] == '*'):
                    res.append(stack.pop())
                stack.append(lst[i])
            if lst[i] == '*':
                while stack and stack[-1] == '*':
                    res.append(stack.pop())
                stack.append(lst[i])
            if lst[i] == ')':
                while stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()
        i += 1
    while stack:
        res.append(stack.pop())

def postfix_count(res):
    stack = []
    i = 0
    while i < len(res):
        if res[i].isdigit():
            stack.append(int(res[i]))
        else:
            if res[i] == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            if res[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
        i += 1

    print(stack[-1])

for tc in range(1, 11):
    N = int(input())
    lst = list(input())
    res = []
    postfix(lst, N)
    print('#{}'.format(tc), end=' ')
    postfix_count(res)


