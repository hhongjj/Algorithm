# D4 3143 가장빠른문자열타이핑
# 해결 안됨.
T = int(input())
for tc in range(1, T + 1):
    A,B = input().rstrip().split()
    print(A,B)
# for tc in range(1, T + 1):
#     A, B = input().split()
#     A = list(A)
#     B = list(B)
#     cnt = 0
#     idx = 0
#     i = 0
#     while i <= len(A):
#         if A[i] == B[idx]:
#             i += 1
#             idx += 1
#             if idx == len(B) - 1:
#                 cnt += 1
#                 idx = 0
#         if A[i] != B[idx]:
#             cnt += idx + 1
#             idx = 0
#             i += 1
#     print('#{} {}'.format(tc, cnt))



    # for i in range(len(A)):
    #     if A[i] == B[idx]:
    #         if idx == len(B) - 1:
    #             idx = 0
    #             cnt += 1
    #         else:
    #             idx += 1
    #     else:
    #         cnt += idx
    #         idx = 0
    #         cnt += 1
    #     if idx != 0 and i == len(A) - 1:
    #         cnt += idx
    # print('#{} {}'.format(tc, cnt))

