# G4 2616 소형기관차
# https://www.acmicpc.net/problem/2616
# 다이나믹 프로그래밍, 누적 합
import sys
from itertools import accumulate
input = sys.stdin.readline

car = int(input())
people = list(map(int, input().split()))
m = int(input())

prefix_sum = list(accumulate(people))
print(prefix_sum)