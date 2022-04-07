# G3 13904 과제
# https://www.acmicpc.net/problem/13904
# 자료 구조, 그리디 알고리즘,우선순위 큐
import sys
input = sys.stdin.readline
N = int(input())
lst = list(list(map(int, input().split())) for _ in range(N))
lst.sort(key=lambda x:x[1], reverse=True)
score = [0]*(1001)
for x, y in lst:
    if not score[x]:
        score[x] = y
    else:
        for i in range(x-1, 0, -1):
            if not score[i]:
                score[i] = y
                break

print(sum(score))