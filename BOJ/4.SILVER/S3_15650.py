# 15650 N과 M (2)

import sys
input = sys.stdin.readline

N, M = map(int,input().split())

res = []
used = [0]*(N+1)
def dfs(res: list, used: list,k):
    global N, M, result
    if len(res) == M:
        result.append(res[:])
        return
    for i in range(k, N+1):
        if used[i]:
            continue
        res.append(i)
        used[i] = 1
        dfs(res, used, i+1)
        res.pop()
        used[i] = 0

result = []
k = 1
dfs(res, used, k)

for i in result:
    print(*i)
