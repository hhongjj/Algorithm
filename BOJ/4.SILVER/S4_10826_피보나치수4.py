# S4 10826 피보나치 수 4

import sys
input = sys.stdin.readline

n = int(input())
a = 0
b = 1
for i in range(2, n+1):
    a, b = b, a+b

if n == 0:
    print(0)
else:
    print(b)