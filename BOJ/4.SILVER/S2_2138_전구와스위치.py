# S2 2138 전구와 스위치
# https://www.acmicpc.net/problem/2138
# 그리디 알고리즘
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip()))
B = list(map(int, input().rstrip()))


def change(k, n):
    for j in range(k, k+n):
        A[j] = 1 - A[j]


cnt = 0
i = 0
while i < N:
    if i < N-2 and A[i] == B[i] and A[i+1] == B[i+1] and A[i+2] == B[i+2]:
        i += 3
    if i == 0:
        if A[i] == B[i] and A[i+1] == B[i+1]:
            i += 2
        elif A[i] == B[i] and A[i+1] != B[i+1]:
            change(i, 2)
            i += 1
            cnt += 1
    if A[i-1] != B[i-1]:
        change(i-1, 3)
        i += 1
        cnt += 1
    if i == N-1:
        if A[i-1] != B[i-1] and A[i-1] != B[i-1]:
            change(i-1, 2)
            cnt += 1
            break
        else:
            break

if A == B:
    print(cnt)
else:
    print(-1)




