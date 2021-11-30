# G3 1248 맞춰봐
# https://www.acmicpc.net/problem/1248
# 백트래킹

def back(idx):
    if idx == N:
        return True
    if S[idx][idx] == '0':
        result[idx] = 0
        return back(idx+1)
    for i in range(1, 11):
        result[idx] = S[idx][idx] * i    # 부호에 해당하는 숫자 넣어줌 (양수 or 음수)
        if check(idx) and back(idx+1):
            return True
    return False

def check(idx):
    num_sum = 0
    for i in range(idx, -1, -1):
        num_sum += result[i]
        if num_sum == 0 and S[i][idx] != 0:
            return False
        elif num_sum < 0 and S[i][idx] >= 0:
            return False
        elif num_sum > 0 and S[i][idx] <= 0:
            return False
    return True

N = int(input())
tmp = list(input())
S = [[0] * N for _ in range(N)]   # [[-1, 1, 0, 1], [0, 1, 1, 1], [0, 0, -1, -1], [0, 0, 0, 1]]
for i in range(N):
    for j in range(i, N):
        temp = tmp.pop(0)
        if temp == '+':
            S[i][j] = 1
        elif temp == '-':
            S[i][j] = -1

result = [0] * N
back(0)
print(' '.join(map(str, result)))






# def back(c, n):
#     if c == N:
#         return
#
#     if check(c):
#         stack.append(0)
#         back(c + 1, n)
#     else:
#         return
#
#     temp = stack.pop()
#     if S[c][0] == '-':
#         stack.append(temp-1)
#     elif S[c][0] == '+':
#         stack.append(temp+1)
#     else:
#         stack.append(temp)

# S = []      # [['-', '+', '0', '+'], ['+', '+', '+'], ['-', '-'], ['+']]
# t = 0
# for i in range(N):
#     S.append(list(tmp[t:t+N-i]))
#     t += N-i
# stack = [4,6,-3,2]
# idx = 3
# for i in range(idx+1):
#     # num_sum = 0
#     for j in range(i, idx+1):
#         print(i, j)
#         num_sum = sum(stack[i:j + 1])
#         print(num_sum)