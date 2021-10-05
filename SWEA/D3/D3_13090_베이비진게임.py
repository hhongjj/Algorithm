# D3 13090 베이비진 게임
# 10개중 8개 맞음.. 왜지?? 어떤걸 놓친 걸까??

def jud(card):
    num = 10
    res = ''
    for c in range(len(card)-2):
        if card[c] + 1 == card[c+1] and card[c+1] + 1 == card[c+2]:
            res = 'run'
            num = c+2
    num_lst = [0] * 10
    for idx, c in enumerate(card):
        num_lst[c] += 1
        if num_lst[c] >= 3:
            if num > idx:
                num = idx
                res = 'triplet'
    return res, num


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    A, B = [], []
    for i in range(len(lst)):
        if i % 2 == 0:
            A.append(lst[i])
        else:
            B.append(lst[i])
    A.sort()
    B.sort()
    res_A = jud(A)
    res_B = jud(B)
    if res_A[1] < res_B[1]:
        print('#{} 1'.format(tc))
    elif res_A[1] == res_B[1]:
        print('#{} 0'.format(tc))
    elif res_A[1] > res_B[1]:
        print('#{} 2'.format(tc))
