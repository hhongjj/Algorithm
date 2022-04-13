# G4 14267 회사 문화 1
# https://www.acmicpc.net/problem/14267
# 다이나믹 프로그래밍, 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색, 트리에서의 다이나믹 프로그래밍
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
employee = [[] for _ in range(n+1)]
for i, num in enumerate(lst[1:]):           # 상사에게 직속 부하 저장
    employee[num].append(i+2)

com = {}
for _ in range(m):                          # dict에 직원 칭찬 중복 저장
    i, w = map(int, input().split())
    if i in com.keys():
        com[i] += w
    else:
        com[i] = w

score = [0]*(n+1)                    
for k, v in com.items():                    # dfs 써서 직속 부하들 score에 점수 계속 더해주기
    deq = deque()
    deq.append(k)
    while deq:
        tmp = deq.popleft()
        deq += employee[tmp]
        score[tmp] += v
print(*score[1:])