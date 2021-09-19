# S5 12787 지금 밥이 문제냐
# https://www.acmicpc.net/problem/12787
# 구현, 문자열, 파싱

# int는 베이스가 기본 십임 그래서 int('1001', 2) - 하면 이진수인걸 10진수로바꿔줌
def change_to_integer(ip):
    ip = ip.split('.')
    x =''
    for i in ip:
        b = format(int(i), 'b')                 # 이진수로 바꾼다.
        if len(str(b)) != 8:                    # 이진수로 바꾼 수가 8자리가 아니면 8자리로 만들어줌
            b = '0'*(8-len(str(b))) + str(b)
        x += b
    result = int(x, 2)                          # 이진수를 십진수로 바꾼다.
    print(result)


def change_to_IPv8(ip):
    b = format(int(ip), 'b')                    # 이진수로 바꾼다.
    if len(b) != 64:                            # 이진수로 바꾼 수를 64자리로 만들어줌.
        b = '0'*(64-len(b)) + b

    result = ''
    for i in range(0, len(b), 8):               # 8개씩 끊어서 십지수로 만들어서 result에 더해준다.
        if i == len(b) - 8:
            result += str(int(b[i:i+8], 2))
        else:
            result += str(int(b[i:i+8], 2)) + '.'
    print(result)


T = int(input())
for _ in range(T):
    address = input().split()
    if address[0] == '1':
        change_to_integer(address[1])
    else:
        change_to_IPv8(address[1])


# 이진수와 십진수를 변환하는 방법을 내장함수를 이용해 쉽게 했지만,
# 만약에 쓰지 않고 하려고 했으면 힘들었을 것 같다.
# 다른 방법이 있는지 생각해보자!