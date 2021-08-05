# 11399 ATM
# 그리디 알고리즘 정렬

import sys
input = sys.stdin.readline

N = int(input())

pi = list(map(int,input().split()))

pi = sorted(pi)
sum = 0
result = 0 
for i in pi:
    sum += i
    result += sum

print(result)

# 오름차순으로 정렬한 후 0번째 있는 Pi는 결국에 n번 더해짐
# i번째는 N-i번 더해짐