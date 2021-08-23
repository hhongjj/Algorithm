# G5 1068 트리

N = int(input())
lst = list(map(int, input().split()))
era = int(input())
tree = [[] for _ in range(N)]

def node(now):
    global cnt
    for i in range(len(tree[now])):
        if tree[now][i] != era:
            stack.append(tree[now][i])

    while stack:
        data = stack.pop()
        if not tree[data]:
            cnt += 1
        node(data)

for i in range(N):
    if lst[i] == -1:
        root = i
    else:
        tree[lst[i]].append(i)
cnt = 0
tree[era] = -2
stack = []
if root != era:                  # root를 지우면 그냥 0
    node(root)
print(cnt)

print(tree)
# list의 각 인덱스가 노드 번호라 생각하고 연결된 노드 번호를 적는다.
# 지울 노드에 해당되는 인덱스의 값을 다 지우고
# root(-1) 부터 시작해서 값을 확인하면서 리프 노드 개수 확인.

# 5
# -1 0 1 2 3
# 1
# 0
# [[1], -2, [3], [4], []]
# 루트 한개는 1로