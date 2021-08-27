# D4 1231 중위순회

def inorder(node):
    if len(tree[node]) >= 3:
        inorder(int(tree[node][2]))
    print(tree[node][1], end='')
    if len(tree[node]) >= 4:
        inorder(int(tree[node][3]))



for tc in range(1,11):
    N = int(input())
    tree = [[]]
    for _ in range(N):
        tree.append(input().split())
    print('#{}'.format(tc), end=' ')
    inorder(1)
    print('')
