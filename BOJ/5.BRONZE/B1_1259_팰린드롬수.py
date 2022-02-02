# B1 1259 팰린드롬수
# https://www.acmicpc.net/problem/1259
# 구현, 문자열

while 1:
    num = input()
    if not int(num):
        break
    if num == num[::-1]:
        print('yes')
    else:
        print('no')
