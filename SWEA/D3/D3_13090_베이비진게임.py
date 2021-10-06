# D3 13090 베이비진 게임
# 10개중 9개 맞음.. 왜지?? 어떤걸 놓친 걸까??

def jud(card):
    num = 10
    stack = card[:2]
    for c in range(2, len(card)):
        stack.append(card[c])
        tmp = sorted(stack)
        for k in range(len(tmp)-2):
            if tmp[k] + 1 == tmp[k+1] and tmp[k+1] + 1 == tmp[k+2]:
                num = c
                break
        if num != 10:
            break
    num_lst = [0] * 10
    for idx, c in enumerate(card):
        num_lst[c] += 1
        if num_lst[c] >= 3:
            if num > idx:
                num = idx
                break
    return num


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    A, B = [], []
    for i in range(len(lst)):
        if i % 2 == 0:
            A.append(lst[i])
        else:
            B.append(lst[i])
    res_A = jud(A)
    res_B = jud(B)
    if res_A == 10 and res_B == 10:
        print('#{} 0'.format(tc))
    elif res_A <= res_B:
        print('#{} 1'.format(tc))
    else:
        print('#{} 2'.format(tc))


