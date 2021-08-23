# D4 1223 계산기2

for tc in range(1,11):
    n = int(input())
    lst = list(input())
    num = []
    stack = []
    sum_lst = 0
    for i in lst:
        if i == '+':
            if stack and stack[-1] == '*':
                n = 0
                while stack:
                    stack.pop()
                    n += 1
                X = 1
                for j in range(n+1):
                    X *= num.pop()
                sum_lst += X
        elif i == '*':
            stack.append(i)
        else:
            num.append(int(i))
    if stack:
        n = 0
        while stack:
            stack.pop()
            n += 1
        X = 1
        for _ in range(n+1):
            X *= num.pop()
        sum_lst += X
    sum_lst += sum(num)
    print('#{} {}'.format(tc, sum_lst))