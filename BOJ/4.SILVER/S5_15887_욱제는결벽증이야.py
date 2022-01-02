# S5 15887 욱제는 결벽증이야!!
# https://www.acmicpc.net/problem/15887
# 구현, 정렬, 구성적

N = int(input())
card = list(map(int, input().split()))
card_sort = sorted(card)

i, op = 0, 0
op_list = list()
while card != card_sort:
    if card[i] != i + 1:
        op += 1
        idx = card.index(i+1) + 1
        card[i:idx] = card[i:idx][::-1]
        op_list.append([i+1, idx])
    i += 1

print(op)
for i in op_list:
    print(*i)
