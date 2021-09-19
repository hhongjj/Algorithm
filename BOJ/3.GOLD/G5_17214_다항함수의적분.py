# G5 17214 다항 함수의 적분
# https://www.acmicpc.net/problem/17214
# 수학, 문자열, 피싱, 미적분학
# 답이 다 맞는 것 같은데 뭐가 문제일까.. 하지만 너무 복잡하니까 간단하게 하는 방법을 찾아보기..
## 0 일경우 W 만 출력
# poly = input().split('x')
#
# if len(poly[0]) == 0:
#
#
# print(poly)
# print(len(poly[1]))

poly = input()
if '+' in poly:
    poly = poly.split('+')
elif '-' in poly:
    if poly[0] == '-':
        poly = poly.split('-')
        if len(poly) == 3:
            poly[0] = '-' + poly[1]
            poly[1] = '-' + poly[2]
            poly.pop()
        else:
            poly[0] = '-' + poly[1]
            poly.pop()
    else:
        poly = poly.split('-')
        poly[1] = '-' + poly[1]
else:
    temp = poly
    poly = list()
    poly.append(temp)

result = ''
for p in range(len(poly)):
    if poly[p] == 'x':                # x만 있을 때
        if len(result):
            result += '+'
        result += '1/2xx'
    elif poly[p] == '-x':             # -x 일 때
        if len(result):
            result += '+'
        result += '-1/2xx'
    elif poly[p][-1] == 'x':          # ax 일 때
        num = ''
        if poly[p][0] == '-':         # -ax 일 때
            result += '-'
            for i in range(1, len(poly[p])-1):
                num += poly[p][i]
            if num == '2':            # 만약 계수가 1이 된다면 1은 생략
                result += 'xx'
            else:
                num = int(num) // 2
                result += str(num) + 'xx'
        else:                        # +ax 일 때
            if len(result):
                result += '+'
            for i in range(len(poly[p])-1):
                num += poly[p][i]
            if num == '2':            # 만약 계수가 1이 된다면 1은 생략
                result += 'xx'
            else:
                num = int(num) // 2
                result += str(num) + 'xx'
    else:                              # 상수일때
        if poly[p][0] == '-':          # 상수가 - 일때
            if poly[p] == '-1':        # 상수가 -1일 떄
                result += '-x'
            else:
                result += poly[p] + 'x'
        else:                          # 상수가 + 일 때
            if len(result):            # 첫번째 항이 아니라면 + 해줌.
                result += '+'
            if poly[p] == '1':           # 상수가 1일 때
                result += 'x'
            else:
                result += poly[p] + 'x'


result += '+W'
print(result)