# S2 1931 회의실 배정
# https://www.acmicpc.net/problem/1931
# 그리디 알고리즘, 정렬
import sys
input = sys.stdin.readline

N = int(input())
time_room = list(list(map(int, input().split())) for _ in range(N))

time_room.sort(key=lambda x: (x[1], x[0]))
end = time_room[0][1]

cnt = 1
for i in range(1, N):
    if time_room[i][0] >= end:
        cnt += 1
        end = time_room[i][1]
print(cnt)


# 종료시간을 오름차순으로 정렬한 후, 시작시간도 오름차순으로 정렬해준다.
# for문을 돌면서 시작시간이 종료시간 보타 크면 카운트 해줌.
