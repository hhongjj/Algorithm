# S1 16206 롤케이크
# https://www.acmicpc.net/problem/16206
# 그리디 알고리즘

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(key=lambda x : (x % 10, x//10))

cnt = 0
i = 0
while i < N:
    p = A[i]
    if p == 10:
        cnt += 1
    elif not p % 10:
        if p // 10 - 1 <= M:
            M -= (p // 10 - 1)
            cnt += p // 10
        else:
            cnt += M
            M = 0
    else:
        if p // 10 <= M:
            M -= p // 10
            cnt += p // 10
        else:
            cnt += M
            M = 0
    i += 1

print(cnt)
# cnt = A.count(10)
# for _ in range(A.count(10)):
#     A.remove(10)
# A.sort(key=lambda x : (x % 10, x//10), reverse=True)
# for i in range(len(A)-1, -1, -1):
#     p = A[i]
#     if not p % 10:
#         if p // 10 - 1 <= M:
#             M -= (p // 10 - 1)
#             cnt += p // 10
#         else:
#             cnt += M
#             M = 0
#         A.remove(p)
#     else:
#         break
#
# rest = []
# while M and len(A):
#     A.sort(reverse=True)
#     x = A.pop()
#     if x < 10:
#         rest.append(x)
#     elif x == 10:
#         cnt += 1
#     else:
#         cnt += 1
#         x -= 10
#         if x == 10:
#             cnt += 1
#         elif x < 10:
#             rest.append(x)
#         else:
#             A.append(x)
#     M -= 1
# # cnt += sum(rest) // 10
# print(cnt)
