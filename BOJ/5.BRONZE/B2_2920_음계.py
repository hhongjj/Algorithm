# B2 2920 음계
# https://www.acmicpc.net/problem/2920
#

import sys
input = sys.stdin.readline
scale = list(map(int, input().split()))


def ascending():
    for i in range(len(scale)):
        if i+1 != scale[i]:
            print('mixed')
            exit()
    print('ascending')


def descending():
    num = 8
    for i in range(len(scale)):
        if num != scale[i]:
            print('mixed')
            exit()
        num -= 1
    print('descending')


if scale[0] == 1:
    ascending()
elif scale[0] == 8:
    descending()
else:
    print('mixed')

