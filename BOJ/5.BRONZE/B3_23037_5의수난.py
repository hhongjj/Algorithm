# B3 23037 5의 수난
# https://www.acmicpc.net/problem/23037

n = list(input())
res = 0
for i in range(len(n)):
    res += int(n[i])**5

print(res)
