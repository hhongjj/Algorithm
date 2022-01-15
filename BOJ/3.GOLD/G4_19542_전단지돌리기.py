# G4 19542 전단지 돌리기
# https://www.acmicpc.net/problem/19542
# 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색

import sys
import numpy
input = sys.stdin.readline

N, S, D = input().split()
N, S, D = int(N), int(S), int(D)
leaf = [0] * (N + 1)
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    leaf[x] += 1
    leaf[y] += 1
    tree[x].append(y)    # [[], [2], [1, 3, 4], [2, 5], [2], [3, 6], [5]] 연결되어 있는 노드 다 저장
    tree[y].append(x)

# leaf = [0, 1, 3, 2, 1, 2, 1] -> 1인 부분이 리프 노드와 root임.
# leaf = numpy.array(leaf)
# leaf = list(numpy.where(leaf == 1)[0])   # numpy.where()매소드 리턴값 (array([1, 4, 6], dtype=int64),)
# leaf.remove(S)   # 루트 노드를 제거

temp = []
for i in range(N+1):
    if i != S and len(tree[i]) == 1:
        temp.append(i)
leaf = temp

def del_leaf():
    global leaf
    print(leaf)
    temp = []
    for i in range(len(leaf)):
        p = tree[leaf[i]][0]
        tree[leaf[i]] = []
        tree[p].remove(leaf[i])
        if len(tree[p]) == 1:
            temp.append(i)
    leaf = temp


# D만큼 리프 노드 에서 가지 쳐내기
for _ in range(D):
    del_leaf()
    # find_leaf()


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
