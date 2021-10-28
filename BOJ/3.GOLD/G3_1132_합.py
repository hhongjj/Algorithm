# G3 1132 합
# https://www.acmicpc.net/problem/1132
# 그리디 알고리즘


def zero():
    global alpha
    sum_num = 0
    idx = 9
    for k, v in alpha.items():      # 우선 각 알파벳의 값을 내림차순으로 9 부터 할당한다.
        num[str(idx)] = k
        idx -= 1

    temp = nonzero[0]               # 0이면 안되고 제일 작은 값을 temp 에 넣는다.
    ix = 1
    while num['0'] == temp:         # 0에 해당하는 알파벳과 계속 자리를 바꿔 가며 0이여도 되는 알파벳을 만나면 바꾸고 끝난다.
        if num[str(ix)] not in nonzero:
            num['0'], num[str(ix)] = num[str(ix)], num['0']
            break
        else:
            num['0'], num[str(ix)] = num[str(ix)], num['0']
            ix += 1
            temp = num['0']

    alpha = dict(alpha)
    for k, v in num.items():            # 할당이 끝났으므로 더한다.
        sum_num += int(k) * alpha[v]

    return sum_num


def big():
    sum_num = 0
    idx = 9
    for k, v in alpha.items():            # 순서대로 할당하면서 더한다.
        num[str(idx)] = k
        sum_num += v * idx
        idx -= 1
    return sum_num


N = int(input())
lst = list(input().rstrip() for _ in range(N))
alpha = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0} # chr(65+i) 로 하기
num = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
nonzero = {}
for i in range(N):  # 자리를 숫자로 표현. {'A': 101, 'B': 110, 'C': 11, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0}
    nonzero[lst[i][0]] = 0            # 0 이 아니여야 하는 맨 앞자리 알파벳
    for j in range(len(lst[i])):
        tmp = alpha[lst[i][j]]
        tmp += 10 ** (len(lst[i]) - j-1)
        alpha[lst[i][j]] = tmp

for key in nonzero.keys():
    nonzero[key] = alpha[key]

alpha = dict(sorted(alpha.items(), key=lambda x: x[1], reverse=True))   # value 값을 기준으로 내림차순으로 정리
nonzero = dict(sorted(nonzero.items(), key=lambda x: x[1]))             # value 값을 기준으로 오름차순으로 정리 -> value 값이 작을수록 0일 확률이 높다.
nonzero = list(nonzero.keys())                                          # key 값만 들고온다.

flag = True
for key, value in alpha.items():
    if value == 0:           # 어떤 알파벳이 0을 나타내야함.
        flag = False
        break

if flag and N > 1:
    res = zero()
else:       # value 가 큰 수 부터 9를 가지면 된다.
    res = big()


print(res)

# 4
# ABCDEFGHIJ
# J
# H
# I
# nonezero {'J': 2, 'I': 11, 'H': 101, 'A': 1000000000}