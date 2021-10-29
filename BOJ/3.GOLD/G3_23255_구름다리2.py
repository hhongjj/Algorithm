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

# 이유를 모르겠다.. 내가 파악하지 못한 조건이 뭘까??
# 7 6
# 1 2
# 5 4
# 3 2
# 3 4
# 5 6
# 6 7
# [[1, 2], [3, 2], [3, 4], [5, 4], [5, 6], [6, 7]]
# 1 2 1 2 1 2 1
