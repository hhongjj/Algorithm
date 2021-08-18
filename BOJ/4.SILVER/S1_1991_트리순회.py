# S1 1991 트리 순회
# 트리, 재귀

import sys
input = sys.stdin.readline

N = int(input())

class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self, root):
        self.root = root

    # 전위 순회
    def preorder(self, node):
        print(node.val, end='')
        if node.left != '.':
            self.preorder(node.left)
        if node.right != '.':
            self.preorder(node.right)

    # 중위 순회
    def inorder(self, node):
        if node.left != '.':
            self.preorder(node.left)
        print(node.val, end='')
        if node.right != '.':
            self.preorder(node.right)

    #후위 순회
    def postorder(self, node):
        if node.left != '.':
            self.preorder(node.left)
        if node.right != '.':
            self.preorder(node.right)
        print(node.val, end='')

for _ in range(N):
    a, b, c = input().split()
    Node(a, Node(b), Node(c))

T1 = BST('A')

T1.preorder('A')