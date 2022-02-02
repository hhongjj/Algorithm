# S5 1018 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
# 브루트포스 알고리즘

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
chess = list(list(input().rstrip()) for _ in range(N))
white, black = 'WBWBWBWB', 'BWBWBWBW'
num = []


def white_chess(x, y):
    global num
    cnt = 0
    for i in range(x, x+8, 2):
        if ''.join(chess[i]) != white:
            for j in range(y, y+8):
                if chess[i][j] != white[j-y]:
                    cnt += 1
    for i in range(x+1, x+8, 2):
        if ''.join(chess[i]) != black:
            for j in range(y, y+8):
                if chess[i][j] != black[j-y]:
                    cnt += 1
    num.append(cnt)


def black_chess(x, y):
    global num
    cnt = 0
    for i in range(x, x + 8, 2):
        if ''.join(chess[i]) != black:
            for j in range(y, y + 8):
                if chess[i][j] != black[j-y]:
                    cnt += 1
    for i in range(x + 1, x + 8, 2):
        if ''.join(chess[i]) != white:
            for j in range(y, y + 8):
                if chess[i][j] != white[j-y]:
                    cnt += 1
    num.append(cnt)


for i in range(N-7):
    for j in range(M-7):
        white_chess(i, j)
        black_chess(i, j)

print(min(num))