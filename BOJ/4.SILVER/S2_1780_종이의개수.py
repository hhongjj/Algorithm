# S2 1780 종이의 개수
# https://www.acmicpc.net/problem/1780
# 분할 정복, 재귀

N = int(input())
lst = list(list(map(int, input().split())) for _ in range(N))

zero, one, minus = 0, 0, 0


def cut(r, c, n):
    global zero, one, minus
    paper = lst[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper != lst[i][j]:
                n //= 3
                cut(r, c, n)
                cut(r, c+n, n)
                cut(r, c+2*n, n)
                cut(r+n, c, n)
                cut(r+n, c+n, n)
                cut(r+n, c+2*n, n)
                cut(r+2*n, c, n)
                cut(r+2*n, c+n, n)
                cut(r+2*n, c+2*n, n)
                return
    if paper == 0:
        zero += 1
    elif paper == 1:
        one += 1
    else:
        minus += 1
    return


cut(0, 0, N)
print(minus)
print(zero)
print(one)

