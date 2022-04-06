# G4 14698 전생했더니 슬라임 연구자였던 건에 대하여 (Hard)
# https://www.acmicpc.net/problem/14698
# 자료구조, 그리디 알고리즘, 우선순위 큐
import heapq, sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    slime = list(map(int, input().split()))
    heapq.heapify(slime)
    num = 1
    while len(slime) > 1:
        x = heapq.heappop(slime)
        y = heapq.heappop(slime)
        z = (x * y) 
        num *= z
        heapq.heappush(slime, z)
    print(num % 1000000007)

# 이건 속도가 조금 더 느림.
# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     slime = sorted(list(map(int, input().split())), reverse=True)
#     if len(slime) == 1:
#         print(1)
#         continue
#     num = 1
#     while len(slime) > 1:
#         x = slime.pop()
#         y = slime.pop()
#         z = x * y
#         num *= z
#         slime.append(z)
#         slime = sorted(slime, reverse=True)
#     print(num % 1000000007)