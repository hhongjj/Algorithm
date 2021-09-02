# G5 2225 합분해
# 아직 ..

N, K = map(int, input().split())

cnt = 0
for i in range(1, N+1):
    stack = []
    stack.append(i)
    while stack:
        for j in range(1, N+1):
            if i == j:
                continue
            if sum(stack) + j < N and len(stack) < K:
                stack.append(j)
            if sum(stack) + j < N and len(stack) >= K:
                stack.pop()
            if len(stack) == K and sum(stack) == N:
                cnt += 1
                stack.pop()

        if len(stack) == K and sum(stack) == N:
            cnt += 1
            break
        else:
            stack.pop()

        print(stack)
print(cnt)
