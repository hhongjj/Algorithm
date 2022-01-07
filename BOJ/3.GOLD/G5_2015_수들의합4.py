# G5 2015 수들의 합 4
# https://www.acmicpc.net/problem/2015
# 자료 구조, 누적 합, 트리를 사용한 집합과 맵
# 더 생각!!

import sys

input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

num, pre = 0, 0
cnt = {0: 1}
for i in range(N):
    pre += A[i]
    if pre - K in cnt:
        num += cnt[pre-K]
    if pre in cnt:
        cnt[pre] += 1
    else:
        cnt[pre] = 1
        
print(num)

# K = p[j] - p[x] 과 dict 을 이용!
# j 번째 숫자를 포함하는 연속합 중 K 값이 되는 경우의 수는 K = p[j] - p[x]를 만족하는 x의 개수와 같다.
# 즉 p[x] = p[j] - K를 만족하는 x의 경우의 수
# cnt[a] = b : 누적합이 a가 되는 경우가 b개

# 시간 초과! 그냥 막 돌림..
# input = sys.stdin.readline
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# num = 0
# for i in range(N):
#     temp = A[i:]
#     prefix_sum = list(accumulate(temp))
#     num += prefix_sum.count(K)
# print(num)
