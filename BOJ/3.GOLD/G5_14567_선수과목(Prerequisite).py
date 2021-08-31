# G5 14567 선수과목(Prerequisite)
# 다이나믹 프로그래밍, 그래프 이론, 위상 정렬

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = [[] for _ in range(N+1)]
res = [1] * (N+1)                # 몇 학기에 들을 것인지 저장
for _ in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)

for i in range(1, N+1):
    for j in range(len(lst[i])):
        if res[i] < res[lst[i][j]]:    # 선수과목이 이미 학기가 전이라면 continue
            continue
        res[lst[i][j]] = max(res[lst[i][j]]+1, res[i]+1)


for i in range(1, N+1):
    print(res[i], end=' ')

# [[], [2, 3], [5], [], [5], [], []]
# 1번이 2, 3의 선수과목