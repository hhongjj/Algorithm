# D3 1221 GNS

T = int(input())
num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(1, T+1):
    tc, N = input().split()
    lst = input().split()
    result = []
    idx = 0
    for i in num:
        idx = lst.count(i)
        for j in range(idx):
            result.append(i)
    print(tc)
    print(*result)

