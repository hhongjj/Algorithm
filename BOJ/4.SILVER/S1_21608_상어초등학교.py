# S1 21608 상어 초등학교
# https://www.acmicpc.net/problem/21608
# 구현
from collections import deque, OrderedDict


def find_pos(lst):
    check = OrderedDict()
    while lst:
        r, c = lst.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if nr < 0 or nr >= N or nc < 0 or nc >= N or pos[nr][nc]:
                continue
            if (nr, nc) in check:
                check[(nr, nc)] += 1
            else:
                check[(nr, nc)] = 1
    # value 값으로 내림차순하고, nr값, nc 값 순으로 오름차순해줌.
    sort_check = sorted(check.items(), key=lambda x: (-x[1], x[0][0], x[0][1]))
    num = 0
    tmp = sort_check[0][1]
    for s in range(len(sort_check)):
        if tmp == sort_check[s][1]:
            num += 1
        else:
            break
    if num == 1:
        return sort_check[0][0]
    else:
        empty = OrderedDict()
        for k in range(num):
            temp = 0
            r, c = sort_check[k][0]
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if nr < 0 or nr >= N or nc < 0 or nc >= N or pos[nr][nc]:
                    continue
                temp += 1
            empty[(sort_check[k][0])] = temp
        sort_empty = sorted(empty.items(), key=lambda x: (-x[1], x[0][0], x[0][1]))
        return sort_empty[0][0]

def empty_pos(num):
    empty = OrderedDict()
    for i in range(N):
        for j in range(N):
            if pos[i][j]:
                continue
            temp = 0
            for d in range(4):
                nr = i + dr[d]
                nc = j + dc[d]
                if nr < 0 or nr >= N or nc < 0 or nc >= N or pos[nr][nc]:
                    continue
                temp += 1
            empty[(i, j)] = temp
    sort_empty = sorted(empty.items(), key=lambda x: (-x[1], x[0][0], x[0][1]))
    return sort_empty[0][0]

N = int(input())

love = OrderedDict()
order = []
for _ in range(N*N):
    lt = list(map(int, input().split()))
    love[lt[0]] = lt[1:]          # key : 학생번호, value : [좋아하는 학생의 번호]
    order.append(lt[0])           # 학생번호 순서 list


pos = [[0]*N for _ in range(N)]   # 학생 자리 배치

i = 0
sn = order[i]
sr, sc = N//2, N//2
pos[sr][sc] = sn             # 첫번째 학생은 가장 중앙에 앉는다.
student = {sn: (sr, sc)}     # 학생번호 : 학생이 앉은 위치
i += 1
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while i < N*N:
    nn = order[i]              # 학생의 번호
    stack = deque()            # 좋아하는 학생이 자리에 앉아있을 경우 좋아하는 학생의 위치
    for j in love[nn]:         # 좋아하는 학생의 번호 리스트
        if j in student:
            stack.append(student[j])
    if stack:
        x, y = find_pos(stack)     # 학생이 어디에 앉아야 하는지 구하는 함수
    else:
        x, y = empty_pos(nn)
    pos[x][y] = nn
    student[nn] = (x, y)       # 자리에 앉았으므로 추가시켜줌.
    i += 1
print(pos)
sat = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        tmp = []
        x, y = student[pos[i][j]]
        for l in love[pos[i][j]]:
            tmp.append(student[l])
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if (nx, ny) in tmp:
                cnt += 1
        if cnt == 4:
            sat += 1000
        elif cnt == 3:
            sat += 100
        elif cnt == 2:
            sat += 10
        elif cnt == 1:
            sat += 1
print(sat)



# 3
# 1 2 5 1 7
# 2 1 9 4 5
# 3 4 5 6 7
# 4 7 8 9 6
# 5 9 8 3 2
# 6 4 8 1 2
# 7 3 8 2 4
# 8 1 2 3 4
# 9 4 5 7 8
# 엄청 오래 걸림?..

