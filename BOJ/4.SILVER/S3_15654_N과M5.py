# S3 15654 N과 M (5)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))

num = sorted(num)
visit = [0] * N
result = []
def back(idx, N, M):
    if idx == M:
        for i in result:
            print(i, end=' ')
        print('')
        return
    for i in range(N):
        if visit[i] == 1:
            continue
        result.append(num[i])
        visit[i] = 1
        back(idx+1, N, M)
        visit[i] = 0
        result.pop()

back(0, N, M)