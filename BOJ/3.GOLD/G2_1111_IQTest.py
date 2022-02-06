# G2 1111 IQ Test
# https://www.acmicpc.net/problem/1111
# 수학, 구현, 브루트포스 알고리즘
# 5퍼 틀림.. 있는 반례는 다해봄!
import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

if len(lst) >= 3:
    if not (lst[1] - lst[0]):
        for i in range(1, len(lst)):
            if lst[i] != lst[i-1]:
                print('B')
                exit()
        print(lst[-1])
        exit()
    elif not (lst[2] - lst[1]) % (lst[1] - lst[0]):
        a = (lst[2] - lst[1]) // (lst[1] - lst[0])
        b = lst[1] - a*lst[0]
        for i in range(1, len(lst)-1):
            a_temp, b_temp = 0, 0
            if not (lst[i] - lst[i-1]):
                for i in range(1, len(lst)):
                    if lst[i] != lst[i - 1]:
                        print('B')
                        exit()
                print(lst[-1])
                exit()
            if not (lst[i+1] - lst[i]) % (lst[i] - lst[i-1]):
                a_temp = (lst[i+1] - lst[i]) // (lst[i] - lst[i-1])
                b_temp = lst[i] - a * lst[i-1]
            if a != a_temp or b != b_temp:
                print('B')
                exit()
        print(a*lst[-1] + b)
        exit()
    elif (lst[2] - lst[1]) % (lst[1] - lst[0]):
        print('B')
        exit()
elif len(lst) == 1:
    print('A')
else:
    if lst[0] == lst[1]:
        print(lst[0])
    else:
        print('A')