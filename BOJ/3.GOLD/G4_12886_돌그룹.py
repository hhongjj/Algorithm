# G4 12886 돌 그룹
# https://www.acmicpc.net/problem/12886
# 그래프 이론, 그래프 탐색, 너비 우선 탐색

A, B, C = map(int, input().split())

if (A+B+C)%3:
    print(0)
    exit()

