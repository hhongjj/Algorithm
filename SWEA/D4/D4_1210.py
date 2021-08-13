# D4 1210 Ladder1

def ladder():
    dc = [1, -1, 0]
    dr = [0, 0, -1]

    while stack:
        for _ in range(len(stack)):
            a, b = stack.pop()
            for j in range(3):
                r = a + dr[j]
                c = b + dc[j]
                if 0 <= c < 100 and 0 <= r < 100 and lst[r][c] and not visited[r][c]:
                    stack.append([r, c])
                    visited[r][c] = 1
                    break
            if r == 0:
                return c

for _ in range(10):
    T = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    stack = []
    visited = [[0]*100 for _ in range(100)]
    for i in range(100):
        if lst[99][i] == 2:
            stack.append([99, i])
            visited[99][i] = 1
    ans = ladder()
    print('#{} {}'.format(T, ans))

# 맨 마지막 줄 2에서 출발하면서 방문하지 않고 범위내에서 1만 찾아서 감.