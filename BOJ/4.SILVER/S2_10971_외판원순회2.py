# S2 10971 외판원 순회 2
# 아직 X
import sys 
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

res = []
visit = [0] * (N+1)
total = []
min_n = 100000000             #W합으로 하기

def back(start, idx, N):
    global min_n
    if idx == N:
        sum_w = 0
        for i in range(1, N):
            if W[res[i-1]][res[i]] == 0:
                continue
            sum_w += W[res[i-1]][res[i]]
        sum_w += W[res[-1]][res[0]]
        if min_n > sum_w:
            min_n = sum_w
        return
    for i in range(N):
        if visit[i]:
            continue
        visit[i] = 1
        res.append(i)
        back(i, N)
        visit[i] = 0
        res.pop()

back(0, N)
print(min_n)

# def back(idx, N):
#     global min_n
#     if idx == N:
#         sum_w = 0
#         for i in range(1, N):
#             if W[res[i-1]][res[i]] == 0:
#                 continue
#             sum_w += W[res[i-1]][res[i]]
#         sum_w += W[res[-1]][res[0]]
#         if min_n > sum_w:
#             min_n = sum_w
#         return
#     for i in range(N):
#         if visit[i]:
#             continue
#         visit[i] = 1
#         res.append(i)
#         back(idx+1, N)
#         visit[i] = 0
#         res.pop()
#
# back(0, N)
# print(min_n)



#
# visited = [0] * N
# result = []

# def back(visited: list, s):
#     global N, W, sum_w
#     if len(sum_w) == 3:
#         sum_w.append(W[s][result[0]])
#         total.append(sum(sum_w))
#         return
#     for i in range(s, N):
#         if visited[i]:
#             continue
#         if not W[s][i]:
#             continue
#         visited[i] = 1
#         sum_w.append(W[s][i])
#         result.append(i)
#         back(visited, i)
#         sum_w.pop()
#         result.pop()
#         visited[i] = 0
#
# total = []
# sum_w = []
# back(visited, 0)
# print(total)



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