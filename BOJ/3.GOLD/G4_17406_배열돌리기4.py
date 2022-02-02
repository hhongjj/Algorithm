# G4 17406 배열 돌리기 4
# https://www.acmicpc.net/problem/17406
# 구현, 브루트포스 알고리즘

from itertools import permutations
import sys, copy
input = sys.stdin.readline

N, M, K = map(int, input().split())
A = [[0]*(M+1)] + list([0]+list(map(int, input().split())) for _ in range(N))
turn = list(list(map(int, input().split())) for _ in range(K))
turn = list(permutations(turn, K))
cnt = []

def move(sr, sc, er, ec):
    global A_temp
    temp = A_temp[sr][sc]
    # 맨 왼쪽
    for i in range(sr, er):
        A_temp[i][sc] = A_temp[i+1][sc]
    # 맨 아래
    for j in range(sc, ec):
        A_temp[er][j] = A_temp[er][j+1]
    # 맨 오른쪽
    for i in range(er, sr, -1):
        A_temp[i][ec] = A_temp[i-1][ec]
    # 맨 윗줄
    for j in range(ec, sc+1, -1):
        A_temp[sr][j] = A_temp[sr][j-1]
    A_temp[sr][sc+1] = temp


while turn:
    A_temp = copy.deepcopy(A)
    lst = turn.pop()
    for r, c, s in lst:
        sr, sc, er, ec = r-s, c-s, r+s, c+s
        while sr != er:
            move(sr, sc, er, ec)
            sr, sc, er, ec = sr + 1, sc + 1, er - 1, ec - 1
    sum_temp = []
    for i in range(1, N+1):
        sum_temp.append(sum(A_temp[i]))
    cnt.append(min(sum_temp))

print(min(cnt))