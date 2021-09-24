# S2 1080 행렬
# https://www.acmicpc.net/problem/1080
# 그리디 알고리즘

N, M = map(int, input().split())
A = list(list(map(int, input())) for _ in range(N))
B = list(list(map(int, input())) for _ in range(N))


# 3x3 뒤집기
def change(i, j):
    for r in range(i, i+3):
        for c in range(j, j+3):
            A[r][c] = 1 - A[r][c]


cnt = 0
for i in range(N-2):              # 줄 바꿈이 가능한 횟수
    for j in range(M-2):          # 가로 줄 이동 가능 횟수
        if A[i][j] != B[i][j]:    # 같지 않다면 뒤집고 카운트 해줌.
            change(i, j)
            cnt += 1
        if A == B:
            break
if A == B:
    print(cnt)
else:
    print(-1)


