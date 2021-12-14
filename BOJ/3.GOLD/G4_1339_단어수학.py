# G4 1339 단어수학
# https://www.acmicpc.net/problem/1339
# 그리디 알고리즘, 브루트포스 알고리즘
# 리스트로 풀기
import sys
input = sys.stdin.readline

N = int(input())
alpha = [0] * 26
for _ in range(N):
    temp = input().rstrip()
    for i in range(len(temp)):
        alpha[ord(temp[i])-65] += 10 ** (len(temp) - i - 1)

alpha.sort(reverse=True)
n = 9
total = 0
for i in range(len(alpha)):
    total += alpha[i]*n
    n -= 1
print(total)

# dict 이용한 풀이
# import sys
# import operator
# input = sys.stdin.readline
# N = int(input())
# alpha = dict()
# for _ in range(N):
#     temp = list(input().rstrip())
#     length = len(temp)
#     for i in range(length):
#         if temp[i] in alpha:
#             tmp = alpha[temp[i]]
#             alpha[temp[i]] = tmp + 10 ** (length - i - 1)
#         else:
#             alpha[temp[i]] = 10 ** (length - i - 1)
#
# alpha_sort = sorted(alpha.items(), key=operator.itemgetter(1), reverse=True)
#
# n = 9
# total = 0
# for i in range(len(alpha_sort)):
#     total += alpha_sort[i][1]*n
#     n -= 1
# print(total)