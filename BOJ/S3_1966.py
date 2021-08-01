# 1966 프린터 큐
# 구현, 자료구조, 시뮬레이션, 큐

import sys
from collections import deque

input = sys.stdin.readline


T = int(input())             # 테스트 케이스

for i in range(T):
    N, M = map(int, input().split())              # N : 문서의 개수, M : 현재 몇번쨰에 놓여있는지
    p_list = list(map(int, input().split()))      # 중요도
    M_p = p_list[M]                               # 찾고싶은 문서의 중요도
    deq = [(idx, j) for idx, j in enumerate(p_list)]    # (인덱스, 중요도) 를 튜플로 리스트에 저장
    deq = deque(deq)                                    # 리스트를 덱으로 바꿈.
    cnt = 0
    while 1:
        max_p = max(deq, key = lambda x : x[1] )               # 중요도가 높은 것을 max_p에 인덱스와 튜플로 저장.
        if deq.index(max_p) != 0:                              # max가 deq맨앞에 없으면 중요도가 제일 높은 거 전까지 rotate를 이용해 뒤로 옮김.
            deq.rotate(-(deq.index(max_p)))
        find_m = deq.popleft()
        cnt += 1
        if M == find_m[0]:
            print(cnt)
            break





# lambda를 이용하는 방법과 enumerate 사용하는 법을 깨달았음.


    