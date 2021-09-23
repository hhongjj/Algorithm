# S2 1931 회의실 배정
# https://www.acmicpc.net/problem/1931
# 그리디 알고리즘, 정렬

N = int(input())
time_room = list(list(map(int, input().split())) for _ in range(N))

time_table =