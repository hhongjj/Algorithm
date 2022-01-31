# G5 20055 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055
# 구현, 시뮬레이션

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
A = deque(map(int, input().split()))
robot = deque()


def move_belt():
    A.rotate(1)


def move_robot():
    num = len(robot)
    while num:
        x = robot.popleft()
        if x + 1 == N - 1:
            num -= 1
            continue
        if A[x+2] and not (x+2) in robot:
            if x + 2 == N - 1:
                A[x+2] -= 1
                num -= 1
                continue
            robot.append(x+2)
            A[x+2] -= 1
        else:
            robot.append(x+1)
        num -= 1


def put_robot():
    if A[0]:
        robot.append(0)
        A[0] -= 1


cnt = 0
while A.count(0) < K:
    move_belt()
    move_robot()
    put_robot()
    cnt += 1

print(cnt)