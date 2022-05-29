# G4 1967 여행가자 
# https://www.acmicpc.net/problem/1976
# 그래프 이론, 자료 구조, 분리 집합
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

dosi = list([] for _ in range(N+1))
parent = list(k for k in range(N+1))

def  find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x] 

def union(x, y):
    global plan_min
    x=find_parent(x)
    y=find_parent(y)
    if x==plan_min or y==plan_min:
        parent[x]=plan_min
        parent[y]=plan_min
    elif x != y:
        parent[max(x, y)] = min(x, y)
        
temp = list(list(map(int, input().split())) for _ in range(N))
plan = list(map(int, input().split()))
plan_min = min(plan)

for i, tmp in enumerate(temp):
    for j, n in enumerate(tmp):
        if n:
            union(i+1, j+1)

for d in plan:
    if plan_min != parent[d]:
        print('NO')
        exit()
print('YES')