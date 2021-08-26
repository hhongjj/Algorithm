# D3 1225 암호생성기
from collections import deque
for _ in range(10):
    tc = int(input())
    lst = deque(map(int, input().split()))
    s = 0
    while lst[-1] > 0:
        # if s == 5:
        #     s = 0
        # s += 1
        s = s % 5 + 1             # 이렇게 나머지를 이용할 수 있음
        lst.append(lst.popleft()-s)

    lst[-1] = 0
    print('#{}'.format(tc), end=' ')
    print(*lst)
