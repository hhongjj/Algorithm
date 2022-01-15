# G5 1240 노드사이의 거리
# https://www.acmicpc.net/problem/1240
# 그래프 이론, 그래프 탐색, 트리, 너비 우선 탐색, 깊이 우선 탐색

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    x, y, z = map(int, input().split())
    tree[x].append([y, z])
    tree[y].append([x, z])


def dfs(v,g, dist):
    global result
    visited[v] = 1
    for i in range(len(tree[v])):
        if not visited[tree[v][i][0]]:
            if tree[v][i][0] == g:
                result = dist + tree[v][i][1]
                return
            else:
                dfs(tree[v][i][0], g, dist + tree[v][i][1])


for _ in range(M):
    s, e = map(int, input().split())
    visited = [0] * (N+1)
    result = 0
    dfs(s, e, 0)
    print(result)


# tree에 연결되어 있는 노드와 거리를 넣음.
# dfs 로 연결되어있는 곳 들어가면서 goal 노드가 나오면 계속 더한 dist를 result에 넣음.