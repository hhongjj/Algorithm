# G5 13164 행복 유치원
# https://www.acmicpc.net/problem/13164
# 그리디 알고리즘, 정렬

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
height = list(map(int, input().split()))

sub = []
for i in range(1, N):
    sub.append(height[i]-height[i-1])
sub.sort()
print(sum(sub[:N-K]))
