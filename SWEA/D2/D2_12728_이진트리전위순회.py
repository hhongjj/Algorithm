# D2 12728 이진 트리 전위 순회

def dfs(now):
    if not now:
        return
    preorder.append(now)
    dfs(left[now])
    dfs(right[now])
    return


T = int(input())
for tc in range(1, T+1):
    V = int(input())
    left = [0 for _ in range(V+1)]
    right = [0 for _ in range(V+1)]
    for _ in range(V-1):
        p, c = map(int, input().split())
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    preorder = []
    dfs(1)
    print('#{}'.format(tc), end=' ')
    print(*preorder)