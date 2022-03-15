# G5 2140 지뢰찾기
# https://www.acmicpc.net/problem/2140
# 구현, 그리디 알고리즘, 시뮬레이션

import sys
input = sys.stdin.readline

N = int(input())
board = list(list(input().rstrip()) for _ in range(N))
# [['1', '1', '1', '0', '0'], ['2', '#', '#', '#', '1'], ['3', '#', '#', '#', '1'], ['2', '#', '#', '#', '1'], ['1', '2', '2', '1', '0']]
visited = [[0]*N for _ in range(N)]
def up_down(f, num, lst):
    dy = [-1, 0, 1]
    y = 0
    for i in lst:
        print(y)
        if i == '0' and num == '0':
            for d in range(3):
                ny = y + dy[d]
                if ny <= 0 or ny >= N-1 or visited[f][ny]:
                    continue
                visited[f][ny]= 1
                board[f][ny] = 0
        elif i == '3' and num =='3':
            for d in range(3):
                ny = y + dy[d]
                if ny == 0 or ny == N-1 or visited[f][ny]:
                    continue
                visited[f][ny] = 1
                board[f][ny] = '*'
        elif i == '2' and num == '2':
            if visited[f][y]:
                continue
            if y == 1:
                visited[f][1], visited[f][2] = 1, 1
                board[f][1], board[f][2] = '*', '*'
            elif y == N-2:
                visited[f][N-2], visited[f][N-3] = 1, 1
                board[f][N-2], board[f][N-3] = '*', '*'
            else:
                visited[f][y] = 1
                board[f][y] = '*'

            # for d in range(3):
            #     ny = y + dy[d]
            #     if ny == 0 or ny == N-1 or visited[f][ny]:
            #         continue
            #     visited[f][ny] = 1
            #     if board[f-1][y-1] == "1":
            #         visited[1][ny-1], visited[1][ny+1] = 1, 1
            #         board[1][ny], board[1][ny+1] = '*', '*'
            #     else:
            #         visited[1][ny-1], visited[1][ny+1] = 1, 1
            #         board[1][ny], board[1][ny-1] = '*', '*'
        elif i == '1' and num =='1':
            
            for d in range(3):
                ny = y + dy[d]
                if ny == 0 or ny == N-1 or visited[1][ny]:
                    continue
                visited[1][ny] = 1
                if board[1][ny-1:ny+2].count('*') >= 1:
                    visited[1][ny+1] = 1
                    board[1][ny+1] = 0
                    continue
                else:
                    visited[1][ny+1] = 1
                    board[1][ny] = '*'
        y += 1

up_down(1, '0', board[0])
up_down(N-2, '0', board[N-1])
up_down(1, '3', board[0])
up_down(N-2, '3', board[N-1])
up_down(1, '2', board[0])
up_down(N-2, '2', board[N-1])
print(board)

        