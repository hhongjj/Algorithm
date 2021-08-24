# D3 12543 부분집합의 합2
#시간초과...
import sys
sys.getrecursionlimit()

T = int(input())
def subset(level, s):
    global cnt
    if level == N:
        if sum(stack) == K:
            cnt += 1
        return
    for i in range(s, 21):
        # if used[i]:
        #     continue
        if i >= K:
            return
        stack.append(i)
        # used[i] = 1
        subset(level+1, s+1)
        stack.pop()
        # used[i] = 0
    return

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    stack = []
    subset(0, 1)
    print('#{} {}'.format(tc, cnt))

