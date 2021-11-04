# G4 23254 나는 기말고사형 인간이야
# https://www.acmicpc.net/problem/23254
# 자료 구조, 그리디 알고리즘, 우선순위 큐
# 100점은 뺴고 아닌거만 다시 push하자
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))  # 점수
b = list(map(int, input().split()))  # 한시간마다 오르는 점수

subject = []
for i in range(M):
    subject.append([a[i], b[i]])

subject = deque(sorted(subject, key=lambda x: x[1], reverse=True))
time, idx, res, turn = 0, 0, 0, 0
while time < 24 * N:
    time_tmp = (100 - subject[idx][0]) // subject[idx][1]  # 최대한 100점 가까이 만들기 위해 필요한 시간
    if time + time_tmp > 24 * N:  # 시간 초과라면 time_tmp 를 남은 시간으로 바꿔준다.
        time_tmp = 24 * N - time
    subject[idx][0] += time_tmp * subject[idx][1]
    # 만약에 오를 점수를 다 받진 못하더라도 100점 까지 남은 점수가 그 다음 과목에서 오를 점수보다 같거나 높으면 100점을 채우고 시간을 높여준다.
    # [[98, 3], [50, 1]] 일 경우 98을 100으로 만들어 버린다.
    if idx + 1 < M and 100 - subject[idx][0] >= subject[idx + 1][1] and time + time_tmp < 24 * N:
        subject[idx][0] = 100
        time_tmp += 1
    if turn and subject[idx][0] != 100:              # 한 바퀴 다돌고 100점 만들어줌.
        res -= subject[idx][0]
        subject[idx][0] = 100
        time_tmp = 1
        res += subject[idx][0]
    elif not turn:
        res += subject[idx][0]

    if res == 100 * M:
        break
    time += time_tmp
    if idx == M - 1:
        turn += 1
        subject.sort(key=lambda x: x[0], reverse=True)
    idx = (idx + 1) % M

result = 0
for i in range(M):
    result += subject[i][0]
print(result)

# 3 5
# 45 50 69 80 25
# 3 5 7 10 5

# def change(lst_a, lst_b):
#     global time
#     res = 0
#     while time > 0 and lst_a:
#         subject_score, hour_score = lst_a.pop()
#         time_tmp = (100 - subject_score) // hour_score  # 최대한 100점 가까이 만들기 위해 필요한 시간
#         if time - time_tmp < 0:
#             time_tmp = time
#         subject_score += time_tmp * hour_score
#         time -= time_tmp
#         if time > 0 and len(lst_a) and 100 - subject_score >= lst_a[-1][1]:
#             subject_score = 100
#             time -= 1
#         if subject_score != 100:
#             lst_b.appendleft([subject_score, hour_score])
#         res += subject_score
#
#     for i in range(len(lst_a)):
#         res += lst_a[i][0]
#
#     return res
#
# N, M = map(int, input().split())
# a = list(map(int, input().split()))  # 점수
# b = list(map(int, input().split()))  # 한시간마다 오르는 점수
# subject = deque()
# for i in range(M):
#     subject.append([a[i], b[i]])
# subject_sort = deque(sorted(subject, key=lambda x: x[1]))
# time = 24 * N
# subject_tmp = deque()   # 만약에 한바퀴 다돌긴 했는데 다 100점이 아니고 시간이 남았을 경우
# result = 0
# result += change(subject_sort, subject_tmp)
# if time > 0 and len(subject_tmp):
#     result += change(subject_tmp, subject_sort)
# print(result)

# time, idx, res, turn = 0, 0, 0, 0
# while time < 24 * N:
#     time_tmp = (100 - subject[idx][0]) // subject[idx][1]  # 최대한 100점 가까이 만들기 위해 필요한 시간
#     if time + time_tmp > 24 * N:  # 시간 초과라면 time_tmp 를 남은 시간으로 바꿔준다.
#         time_tmp = 24 * N - time
#     subject[idx][0] += time_tmp * subject[idx][1]
#     # 만약에 오를 점수를 다 받진 못하더라도 100점 까지 남은 점수가 그 다음 과목에서 오를 점수보다 같거나 높으면 100점을 채우고 시간을 높여준다.
#     # [[98, 3], [50, 1]] 일 경우 98을 100으로 만들어 버린다.
#     if idx + 1 < M and 100 - subject[idx][0] >= subject[idx + 1][1] and time + time_tmp < 24 * N:
#         subject[idx][0] = 100
#         time_tmp += 1
#     if turn and subject[idx][0] != 100:              # 한 바퀴 다돌고 100점 만들어줌.
#         res -= subject[idx][0]
#         subject[idx][0] = 100
#         time_tmp = 1
#         res += subject[idx][0]
#     elif not turn:
#         res += subject[idx][0]
#
#     if res == 100 * M:
#         break
#     time += time_tmp
#     if idx == M - 1:
#         turn += 1
#         subject.sort(key=lambda x: x[0], reverse=True)
#     idx = (idx + 1) % M