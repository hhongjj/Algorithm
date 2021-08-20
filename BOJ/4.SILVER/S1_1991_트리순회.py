# S1 1991 트리 순회
# 트리, 재귀

import sys
input = sys.stdin.readline

N = int(input())
tree = {}
#################### dfs
# def preorder(tree, root):
#     stack = []
#     stack.append(root)
#     res = ''
#     while len(stack):
#         data = stack.pop()
#         res += data
#         # 오른쪽 자식 체크
#         if tree[data][1] != '.':
#             stack.append(tree[data][1])
#         # 왼쪽 자식 체크
#         if tree[data][0] != '.':
#             stack.append(tree[data][0])
#     print(res)

###### 재귀
def preorder(tree, root):
    print(root, end='')
    if tree[root][0] != '.':
        preorder(tree, tree[root][0])
    if tree[root][1] != '.':
        preorder(tree, tree[root][1])

def inorder(tree, root):
    if tree[root][0] != '.':
        inorder(tree, tree[root][0])
    print(root, end='')
    if tree[root][1] != '.':
        inorder(tree, tree[root][1])

def postorder(tree, root):
    if tree[root][0] != '.':
        postorder(tree, tree[root][0])
    if tree[root][1] != '.':
        postorder(tree, tree[root][1])
    print(root, end='')

for _ in range(N):
    a, b, c = input().split()
    tree[a] = [b, c]


preorder(tree, 'A')
print('')
inorder(tree, 'A')
print('')
postorder(tree, 'A')


# dfs로도 preorder를 해봤지만 그냥 재귀로 함.