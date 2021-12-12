# G4 1339 단어수학
# https://www.acmicpc.net/problem/1339
# 그리디 알고리즘, 브루트포스 알고리즘
import sys
import operator
input = sys.stdin.readline

N = int(input())
alpha = dict()
for _ in range(N):
    temp = list(input().rstrip())
    length = len(temp)
    for i in range(length):
        if temp[i] in alpha:
            tmp = alpha[temp[i]]
            alpha[temp[i]] = tmp + 10 ** (length - i - 1)
        else:
            alpha[temp[i]] = 10 ** (length - i - 1)

alpha_sort = sorted(alpha.items(), key=operator.itemgetter(1), reverse=True)

n = 9
total = 0
for i in range(len(alpha_sort)):
    total += alpha_sort[i][1]*n
    n -= 1
print(total)
