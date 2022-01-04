# G4 12970 AB
# https://www.acmicpc.net/problem/12970
# 수학, 구현, 그리디 알고리즘, 구성적
# 아직 안됨.

N, K = map(int, input().split())
lst = ['B'] * N
ans = []
cnt, flag = 0, 1

idx = N - 1
while cnt != K:
    lst[idx] = 'A'
    ans.append(idx)
    cnt = 0
    for i in range(len(ans)):
        cnt += N - ans[i] - 1 - i
    if idx == 0:
        idx = N - 1
    if cnt != K:
        lst[idx] = 'B'
        ans.pop()

    idx -= 1
    if len(ans) == N:
        flag = 0
        break

if flag:
    print(*lst)
else:
    print(-1)
