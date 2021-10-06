# D3 13110 병합 정렬


def merge(arr):
    global cnt
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge(arr[:mid])
    right = merge(arr[mid:])

    if left[-1] > right[-1]:
        cnt += 1

    tmp = []
    x, y = 0, 0
    while x < len(left) and y < len(right):
        if left[x] < right[y]:
            tmp.append(left[x])
            x += 1
        else:
            tmp.append(right[y])
            y += 1
    # 남아 있는 배열은 정렬되어 있으므로 그냥 다 더해버린다.
    while len(left) > x:
        tmp.append(left[x])
        x += 1
    while len(right) > y:
        tmp.append(right[y])
        y += 1

    return tmp


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    m_l = merge(lst)
    print('#{} {} {}'.format(tc, m_l[N//2], cnt))
