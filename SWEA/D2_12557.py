# D2 12557 특별한 정렬

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))
    result = []
    cnt = 10
    while cnt:
        max_num = 0
        min_num = 101
        for i in range(len(ai)):
            if ai[i] > max_num:
                max_num = ai[i]
                idx_max = i
            if ai[i] < min_num:
                min_num = ai[i]
                idx_min = i
        result.append(max_num)
        result.append(min_num)
        cnt -= 2
        if cnt == 0:
            break
        if idx_max > idx_min:       # pop하면 index가 바뀌니까 뒤에거 부터 pop
            ai.pop(idx_max)
            ai.pop(idx_min)
        else:
            ai.pop(idx_min)
            ai.pop(idx_max)
    print('#{}'.format(tc), end=' ')
    print(*result)


# 제일 큰수랑 제일 작은수랑 뽑아서 새로운 리스트에 추가하고 pop해서 원래 리스트에서 제거
# 다른 방법을 사용해보자!

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     ai = list(map(int, input().split()))
#     cnt = 10
#     for i in range(N):
#         if i % 2 == 0:
#             for j in range(i, N):
#                 if ai[i] < ai[j]:
#                     ai[i], ai[j] = ai[j], ai[i]
#         else:
#             for j in range(i, N):
#                 if ai[i] > ai[j]:
#                     ai[i], ai[j] = ai[j], ai[i]
#     print('#{}'.format(tc), end=' ')
#     for i in range(10):
#         print(ai[i], end=' ')
#     print('')

