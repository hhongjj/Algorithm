# D2 12710 노드의 거리
from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    visited = [0]*(V+1)
    while queue:
        now = queue.popleft()
        for next in range(1, V+1):
            if not adj[now][next] or visited[next]:
                continue
            visited[next] = visited[now] + 1              # visited에 S부터 각 노드까지의 거리를 저장한다
            queue.append(next)
    return visited[G]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj[a][b] = 1
        adj[b][a] = 1
    S, G = map(int, input().split())
    cnt = bfs(S)
    print('#{} {}'.format(tc, cnt))
