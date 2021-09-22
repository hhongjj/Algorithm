# G5 10830 행렬 제곱
# https://www.acmicpc.net/problem/10830
# 수학, 분할 정복, 분할 정복을 이용한 거듭제곱, 선형대수학
#

def multi(c, d):
    ans = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                ans[i][j] += c[i][k] * d[k][j]
            ans[i][j] %= 1000
    return ans


def matrix(b, mat):
    if b == 1:
        return mat
    elif b == 2:
        return multi(mat, mat)
    else:
        temp = matrix(b//2, mat)
        if b % 2 == 0:
            return multi(temp, temp)
        else:
            return multi(multi(temp, temp), mat)
0

N, B = map(int, input().split())
A = list(list(map(int, input().split())) for _ in range(N))

res = matrix(B, A)

for i in range(N):
    for j in range(N):
        print(res[i][j], end=' ')
    print('')