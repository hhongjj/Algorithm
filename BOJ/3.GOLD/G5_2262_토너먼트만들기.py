# G5 2262 토너먼트 만들기
# https://www.acmicpc.net/problem/2262
# 그리디 알고리즘
import sys
input = sys.stdin.readline

n = int(input())
ranking = list(map(int, input().split()))

sum_min = 0
while len(ranking) > 1:
    p = max(ranking)
    idx = ranking.index(p)
    if not idx:
        sum_min += p - ranking[idx+1]
    elif idx == len(ranking)-1:
        sum_min += p - ranking[idx-1]
    else:
        sum_min += p - max(ranking[idx-1], ranking[idx+1])
    ranking.remove(p)

print(sum_min)