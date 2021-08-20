# S1 5639 이진 검색 트리

tree = [50,30,24,5,28,45,98,52,60]

# tree = {}
# def preorder(tree, order, lst):
#     tree
root = tree[0]
left = []
def order(root, be, now):
    global left
    if root > tree[now]:
        if tree[be] > tree[now]:
            left.append(tree[now])
            order(root, now, now+1)
        else:
            print(left.pop())
            # if stack[-1] < tree[now]:
            print(tree[now])
            order(root, now, now+1)
    else:
        while len(left):
            print(left.pop())
        if tree[be] > tree[now]:
            left.append(tree[now])
            order(root, now, now + 1)
        else:
            print(left.pop())
            # if stack[-1] < tree[now]:
            print(tree[now])
            order(root, now, now + 1)






    return





order(root,0,1)
# ans= [5 28 24 45 30 60 52 98 50]v