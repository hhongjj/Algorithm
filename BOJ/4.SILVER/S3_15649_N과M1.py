# S3 15649 N과 M (1)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
res = []
visit = [0] * (N+1)

def back(idx, N, M):
    if idx == M:
        for i in res:
            print(i, end=' ')
        print('')
        return

    for i in range(N):
        if visit[i] == 0:
            visit[i] = 1
            res.append(i+1)
            back(idx+1, N, M)
            visit[i] = 0
            res.pop()


back(0, N, M)