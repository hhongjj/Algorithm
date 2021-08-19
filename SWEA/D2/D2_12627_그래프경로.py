#D2 12627 그래프 경로

T = int(input())

def dfs(S, G):
    global check
    if S == G:
        check = 1
        return
    for next in range(1, V+1):
        if adj[S][next] == 1 and visit[next] == 0:
            visit[next] = 1
            dfs(next, G)
    return

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [
        [0 for _ in range(V+1)] for _ in range(V+1)
    ]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a][b] = 1
    S, G = map(int, input().split())
    visit =[0]*(V+1)
    check = 0
    dfs(S, G)
    print('#{} {}'.format(tc, check))
