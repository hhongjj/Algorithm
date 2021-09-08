# S1 9205 맥주 마시면서 걸어가기
# 그래프 이론, 그래프 탐색, 너비 우선 탐색, 플로이드-와샬
# 아직....수정중
from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    store = deque()
    # 출발점(집)
    sr, sc = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        store.append((x, y))
    # 도착점(페스티벌)
    er, ec = map(int, input().split())
    print(lst)
    sr, sc = lst.popleft()
    go = 1
    while lst:
        er, ec = lst.popleft()
        if abs(sr - er) + abs(sc - ec) > 1000:
            go = 0
            break
        else:
            sr, sc = er, ec

    if go:
        print('happy')
    else:
        print('sad')


# 1
# 2
# 0 0
# -1000 0
# 1000 0
# 1000 1000
# happy 나와야지