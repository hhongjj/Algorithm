# S2 23349 졸업 사진
# https://www.acmicpc.net/problem/23349
# 이름이 같은 경우 제거해야함.... 이름을 키로 하고 나머지를 value로 한다음
# 이름이 같으면 저장안하고 받아온 다음에 list로 만들고 그이후에
# 장소 갯수랑 다시 최저 시간이랑 제일 끝시간을 구해서
# 다시 table을 만들어서 다시 저장하기..........

N = int(input())
lst, place, st_time, et_time = {}, [], [], []
for _ in range(N):
    n, p, st, et = input().split(' ')
    if n in lst:
        continue
    lst[n] = [p, int(st), int(et)]
    place.append(p)
    st_time.append(int(st))
    et_time.append(int(et))

lst = list(lst.values())
# print(lst)
lst_sort = sorted(lst, key=lambda x: x[0])
# print(lst_sort)

fav_place_num = len(set(place))

time_min = min(st_time)
time_max = max(et_time)
table = [[0]*(time_max - time_min) for _ in range(fav_place_num)]
# print(time_max - time_min)

name = lst_sort[0][0]
idx = 0
for i in range(len(lst_sort)):
    if name != lst_sort[i][0]:
        name = lst_sort[i][0]
        idx += 1
    for j in range(lst_sort[i][1]-time_min, int(lst_sort[i][2])-time_min):
        table[idx][j] += 1

print(table)

idx_max = 0
# for i in range(len(table)):
    #