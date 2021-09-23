# S2 11047 동전 0
# https://www.acmicpc.net/problem/11047
# 그리디 알고리즘

from collections import deque

N, K = map(int, input().split())
money = deque()
for _ in range(N):
    money.append(int(input().strip()))

cnt = 0
while K:
    temp = money.pop()
    if K // temp:
        cnt += K // temp
        K -= temp * (K // temp)

print(cnt)


# 큰 동전 부터 K을 나눌 수 있다면 몫 만큼 횟수를 더하고,
# K에서 뺄 수 있는 만큼 빼는 것을 반복한다.
