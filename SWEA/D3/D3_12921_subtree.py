# D3 12921 subtree

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    tree = [[] for _ in range(E+2)]
    for i in range(0, 2*E, 2):
        tree[lst[i]].append(lst[i+1])
    stack = []
    cnt = 1
    for i in range(len(tree[N])):
        stack.append(tree[N][i])
        cnt += 1
    while stack:
        temp = stack.pop()
        for i in range(len(tree[temp])):
            stack.append(tree[temp][i])
            cnt += 1
    print(f'#{tc} {cnt}')

# tree 리스트에 부모 노드 index에 자식 노드 번호를 추가시킨다.
# 부모 노드 부터 출발해서 stack에 추가하고 하나씩 pop하면서 자식노드로 이동한다.
# stack에 추가할 때 노드의 개수를 세어주고 stack이 비어있다면 자식노드를 다 방문 했으므로 끝난다.
