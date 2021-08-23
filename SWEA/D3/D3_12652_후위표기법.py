# D3 12652 후위표기법
# 아직 X
T = int(input())
priority = {'+': 1, '-': 1, '*' : 2, '/': 2, '(' : 0 }
for tc in range(1, 1+T):
    lst = list(input().rstrip())
    stack = []
    print('#{}'.format(tc), end=' ')
    for i in lst:
        if i.isdigit():
            print(i, end='')
        else:
            if not stack:
                stack.append(i)
            if priority[stack[-1]] < priority[i]:
                stack.append(i)
            
            elif i == ')':
                while stack[-1] == '(':
                    print(stack.pop(), end='')
                stack.pop()
            

