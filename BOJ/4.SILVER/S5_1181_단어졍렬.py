# S5 1181 단어 정렬
# https://www.acmicpc.net/problem/1181
# 문자열 정렬

import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(input().rstrip())
lst = list(set(lst))
lst = sorted(lst, key= lambda x: (len(x), x))
for l in lst:
    print(l)