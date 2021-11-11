# B3 23348 스트릿 코딩 파이터
# https://www.acmicpc.net/problem/23348
# 수학, 구현, 사칙연산

import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
N = int(input())
dongari = list(list(map(int, input().split())) for _ in range(3*N))

score = 0
for i in range(N):
    tmp = 0
    for j in range(i*3, (i*3)+3):
        tmp += A * dongari[j][0] + B * dongari[j][1] + C * dongari[j][2]
    if tmp > score:
        score = tmp

print(score)
