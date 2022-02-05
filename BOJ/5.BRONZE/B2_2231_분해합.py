# B2 2231 분해합
# https://www.acmicpc.net/problem/2231
# 브루트포스 알고리즘

N = input()
target = int(N)
min_num = max(1, target - 9*(len(N)))
for i in range(min_num, target):
    result = i + sum(map(int, str(i)))
    if result == target:
        print(i)
        break
else:
    print(0)
