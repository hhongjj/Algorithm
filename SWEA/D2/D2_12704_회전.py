# D2 12704 회전

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [0] * 2000
    num = list(map(int, input().split()))
    for i in range(N):
        lst[i] = num[i]
    front = 0
    rear = N
    while M:
        lst[rear] = lst[front]
        rear += 1
        front += 1
        M -= 1
    print('#{} {}'.format(tc, lst[rear-N]))



# front와 rear를 이용해서 회전시키기.