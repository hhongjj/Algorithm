# S2 10971 외판원 순회 2

import sys 
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

visited = [0] * N


def back(visited: list, s):
    global N, W, start, sum_w
    if len(sum_w) == 3:
        print(s, start)
        sum_w.append(W[s][start])
        total.append(sum(sum_w))
        return
    for i in range(s, N):
        if visited[i]:
            continue
        if not W[s][i]:
            continue
        visited[i] = 1
        sum_w.append(W[s][i])
        back(visited, i)
        visited[i] = 0

total = []

for s in range(N):
    sum_w = []
    start = s
    visited[start] = 1
    back(visited, s)
    print(sum_w)



# def dfs(W: list, total: list, visited: list, deq: deque, sum_w):
#     global N
#     if visited.count(1) == 3:
#         total.append(sum_w)
#         return
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if visited[i]:
#             continue
#         deq.append(i)
#         visited[i] = 1
#         sum += W[i]


# def dfs(deq: list, visited: list, s):
#     global N, W
#     if len(deq) == 4:
#         sum_w = 0
#         for j in range(3):
#             sum_w += W[deq[j] - 1][deq[j + 1] - 1]
#         sum_w += W[deq[-1] - 1][deq[0] - 1]
#         total.append(sum_w)
#         return
#     for i in range(s, N+1):
#         if visited[i] and not W[deq[-1]-1][i-1]:
#             continue
#         deq.append(i)
#         visited[i] = 1
#         dfs(deq, visited, i+1)
#         deq.pop()
#         visited[i] = 0
#
#
# s = 1
# total = []
# sum_w = 0
# dfs(deq, visited, s)
# print(total)

#
# def dfs(deq: list, visited: list, s):
#     global N, W
#     if len(deq) == 4:
#         sum_w = 0
#         for j in range(3):
#             sum_w += W[deq[j]][deq[j + 1]]
#         sum_w += W[deq[-1]][deq[0]]
#         total.append(sum_w)
#         return
#     for i in range(s, N):
#         if visited[i] and not W[deq[-1]][i-1]:
#             continue
#         deq.append(i)
#         visited[i] = 1
#         dfs(deq, visited, i+1)
#         deq.pop()
#         visited[i] = 0
#
#
# s = 0
# total = []
# sum_w = 0
# dfs(deq, visited, s)
# print(total)

# N = 4
# W = [[0, 10, 15, 20],
# [5, 0, 9, 10],
# [6, 13, 0, 12],
# [8, 8, 9, 0]
#     ]