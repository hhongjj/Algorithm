# B2 2775 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
# 수학, 구현

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    lst = list(i for i in range(n+1))
    for _ in range(k):
        for j in range(1, n+1):
            lst[j] += lst[j-1]
    print(lst[-1])
