# B3 1085 직사각형에서 탈출
# https://www.acmicpc.net/problem/1085
# 수학, 기하학

x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))
