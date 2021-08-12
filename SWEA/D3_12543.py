# 12543 부분집합의 합
T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    ans = 0
    for bit in range(1 << 12):
        sum_subset = 0                    # 부분집합 원소 합
        cnt = 0  # 부분집합 크기
        for j in range(12):
            if bit & (1 << j) != 0:
                sum_subset += j+1
                cnt += 1
        if cnt == N and sum_subset == K:  # 원하는 조건에 만족한다면
            ans += 1

    print('#{} {}'.format(tc, ans))