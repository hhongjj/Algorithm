# G3 23255 구름다리 2
# https://www.acmicpc.net/problem/23255
# 그래프 이론, 그리디 알고리즘
# 미완성
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
bridge = list(list(map(int, input().split())) for _ in range(M))
bridge.sort(key=lambda x: (x[0], x[1]))

building = [1]*(N+1)
for i in range(M):
    if building[bridge[i][0]] == building[bridge[i][1]]:
        if bridge[i][0] < bridge[i][1]:
            building[bridge[i][1]] += 1
        else:
            building[bridge[i][0]] += 1
print(*building[1:])

# 반례를 찾았다...
# 4 4
# 1 2
# 2 3
# 2 4
# 3 4
# 1 2 1 2