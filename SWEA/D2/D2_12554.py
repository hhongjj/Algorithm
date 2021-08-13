# D2 12554 이진탐색

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    left = 1
    right = P
    A_cnt = B_cnt = 0
    while left <= right:
        mid = (left + right) // 2
        if A == mid:
            A_cnt += 1
            break
        if A < mid:
            right = mid
            A_cnt += 1
        elif mid < A:
            left = mid
            A_cnt += 1
    left = 1
    right = P
    while left <= right:
        mid = (left + right) // 2
        if B == mid:
            B_cnt += 1
            break
        if B < mid:
            right = mid
            B_cnt += 1
        elif mid < B:
            left = mid
            B_cnt += 1
    if A_cnt > B_cnt:
        print('#{} B'.format(tc))
    elif B_cnt > A_cnt:
        print('#{} A'.format(tc))
    else:
        print('#{} 0'.format(tc))
