# G4 18119 단어암기
# https://www.acmicpc.net/problem/18119
# 브루트포스 알고리즘, 비트마스킹
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
alpha = [set() for _ in range(26)]
for i in range(N):
    word = set(input().rstrip())
    for w in word:
        alpha[ord(w)-97] |= set([i])

one = []
result = set(list(i for i  in range(N)))
for _ in range(M):
    x, y = input().split()
    if x == '1':
        result -= alpha[ord(y)-97]
        one.append(y)
    else:
        one.remove(y)
        result = set(list(i for i  in range(N)))
        for o in one:
            result -= alpha[ord(o)-97]
    print(len(result))


# 두번째 방법
# N, M = map(int, input().split())
# words = list(input().rstrip() for _ in range(N))
# alpha = []
# for i in range(97,123):
#     tmp = []
#     for idx, j in enumerate(words):
#         if chr(i) in j:
#             tmp.append(idx)
#     alpha.append(set(tmp))

# one = []
# result = set(list(i for i  in range(N)))
# for _ in range(M):
#     x, y = input().split()
#     if x == '1':
#         result -= alpha[ord(y)-97]
#         one.append(y)
#     else:
#         one.remove(y)
#         result = set(list(i for i  in range(N)))
#         for o in one:
#             result -= alpha[ord(o)-97]
#     print(len(result))


# 첫번째 방법
# N, M = map(int, input().split())
# words = []
# check = list([0]*(26) for _ in range(N))
# for i in range(N):
#     word = input().rstrip()
#     for j in range(97, 123):
#         if chr(j) in word:
#             check[i][j-97] = 1
#     words.append((word, sum(check[i])))

# for _ in range(M):
#     x, y = input().split()
#     cnt = 0 
#     for i in range(N):
#         if y in words[i][0]:
#             check[i][ord(y)-97] = ord(x) - 49

#         if words[i][1] == sum(check[i]):
#             cnt += 1
#     print(cnt)