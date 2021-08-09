# 1260 DFS와 BFS
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m, v = map(int, input().split())

node = [[0]*(n+1) for _ in range(n+1)]       # (n+1) x (n+1) 의 배열을 만들어 연결된 정점들에 1를 넣는다.
for i in range(m):
    a, b = map(int,input().split())
    node[a][b] = node[b][a] = 1

visited1 = [0]*(n+1)

def dfs(v):
    visited1[v] = 1           # 방문했으면 1
    print(v, end = ' ')
    for i in range(1, n+1):
        if not visited1[i] and node[v][i]:
            dfs(i)

visited2 = [0]*(n+1)

def bfs(v):
    que = [v]
    visited2[v] = 1
    while que:
        v = que.pop(0)
        print(v, end = ' ')
        for i in range(1, n+1):
            if not visited2[i] and node[v][i]:
                que.append(i)
                visited2[i] = 1

dfs(v)
print('')
bfs(v)


# 이론적으로는 이해가 가지만 구현하는 부분이 어렵다.
# 다양한 문제들을 풀어봐야 할듯.
# 방법들이 여러가지인데 여러 방법들을 해봐야할듯