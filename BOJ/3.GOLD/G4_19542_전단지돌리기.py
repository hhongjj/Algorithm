# G4 19542 전단지 돌리기
# https://www.acmicpc.net/problem/19542
# 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색
# 시간 초과
import sys
input = sys.stdin.readline

N, S, D = input().split()
N, S, D = int(N), int(S), int(D)
leaf = []
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)    # [[], [2], [1, 3, 4], [2, 5], [2], [3, 6], [5]] 연결되어 있는 노드 다 저장
    tree[y].append(x)


def find_leaf():
    global leaf
    temp = []
    for i in range(1, N+1):
        if i != S and len(tree[i]) == 1:
            temp.append(i)
    leaf = temp


def del_leaf():
    for i in range(len(leaf)):
        p = tree[leaf[i]][0]
        tree[leaf[i]] = []
        tree[p].remove(leaf[i])


# D만큼 리프 노드 에서 가지 쳐내기
for _ in range(D):
    find_leaf()
    del_leaf()


def dfs(s):
    global dist
    if visited[s]:
        return
    visited[s] = 1
    for i in range(len(tree[s])):
        if not visited[tree[s][i]]:
            dist += 1
            dfs(tree[s][i])
            dist += 1


dist = 0
visited = [0] * (N + 1)
dfs(S)
print(dist)
