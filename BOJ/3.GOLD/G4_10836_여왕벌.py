# G4 10836 여왕벌
# https://www.acmicpc.net/problem/10836
# 구현, 시뮬레이션
# python3으로 제출하면 83점..

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
larva = [1] * (2*M-1)      # 맨 왼쪽 + 맨 위쪽의 자라는 애벌레 수열
for _ in range(N):
    a, b, c = map(int, input().split())
    idx = 0
    for i in range(a, a+b):           # +1 만큼 자라는 애벌레
        larva[i] += 1
    for i in range(a+b, a+b+c):       # +2 만큼 자라는 애벌레
        larva[i] += 2

beehive = larva[M:]                    # 1열부터는 0행과 값이 같으므로
print(*larva[M-1:])                    # 0행 출력
for i in range(M-1):
    print(larva[M-2-i], end=' ')       # 만들어놓은 애벌레 중간이 M-2 니까 거기서부터 앞으로 하나씩
    print(*beehive)
