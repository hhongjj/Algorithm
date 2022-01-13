# S1 15805 트리 나라 관광 가이드
# https://www.acmicpc.net/problem/15805
# 그래프 이론, 그래프 탐색, 트리

import sys
input = sys.stdin.readline
N = int(input())
nara = list(map(int, input().split()))
# tree[x]가 -2 라면 처음 온 노드니까 그 부모는 바로 그 직전에 나온 노드.
tree = [-2] * (max(nara) + 1)
tree[nara[0]] = -1
for i in range(1, len(nara)):
    if tree[nara[i]] == -2:
        tree[nara[i]] = nara[i-1]
print(len(tree))
print(*tree)
