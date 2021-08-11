# S2 10971 외판원 순회 2

import sys 
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

visited = [0]*(N+1)
deq = []

def dfs(deq: list, visited: list,s, sum_w, total: list):
    global N, W
    if len(deq)==4:
        print('deq=4', deq, sum_w)
        sum_w += W[deq[-1]-1][deq[0]-1]
        total.append(sum_w)
        return
    for i in range(s, N+1):
        if visited[i] and not W[deq[-1]][i]:
            continue
        deq.append(i)
        visited[i] = 1
        dfs(deq, visited, i+1, sum_w, total)
        sum_w += W[deq[-2]-1][deq[-1]-1]
        print(sum_w)
        deq.pop()
        visited[i] = 0


s = 1
total = []
sum_w = 0
dfs(deq, visited,s,sum_w,total)
print(total)

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