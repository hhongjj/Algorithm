# G4 1967 트리의 지름
# 그래프 이론, 그래프 탐색, 트리, 깊이 우선 탐색
# 메모리 초과...


n = int(input())
tree = [[0] * (n+1) for _ in range(n+1)]

def dfs(st, now):
    global ans, end, res
    if res > ans:
        ans = res
        end = now
    for i in range(1, n+1):
        if tree[now][i] and st != i:
            res += tree[now][i]
            dfs(now, i)
            res -= tree[now][i]

# 2차원 배열에 부모-자식 가중치를 나타낸다.
tree = dict()
for i in range(1, n+1):
    tree[i] = []
for _ in range(n-1):
    a, b, w = map(int, input().split())
    tree = dict()
    tree[a].append([b, w])
    tree[b] = [a, w]
#...dict 추가하는 방법!!! 뭐야!!!


    # tree[a][b] = w
    # tree[b][a] = w

print(tree)
# 루트부터 제일 긴것 찾기
ans = 0
res = 0
end = 0
# dfs(1,1)


# 루트에서 젤 끝 부분을 end에 저장되어있으므로 end에서 제일 멀리 있는 노드를 찾는다
ans = 0
# dfs(end, end)
print(ans)

# 스택과 재귀를 함께 쓰니 메모리 초과가 뜬다
# 그래서 트리 빼고 배열 자체를 안쓰려고 해봤지만 트리 자체가 메모리를 엄청 많이 쓰는 것 같아 dict으로 구현
