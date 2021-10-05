# S1 5904 Moo 게임
# https://www.acmicpc.net/problem/5904
# 분할 정복, 재귀
import sys
sys.setrecursionlimit(10**6)

N = int(input())

res = 'moo'
def moo(n):
    global res
    if n == N:
        return
    else:
        res += 'm' + 'o' * (n + 3) + res
        moo(n + 1)


moo(0)
print(res[N-1])
# def moo(n):
#     if n == 0:
#         return 'moo'
#     else:
#         x = moo(n-1)
#         return x+'m'+'o'*(n+2)+x
#
#
# print(moo(N)[N-1])
