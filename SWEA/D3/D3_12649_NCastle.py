# D3 12649 N Castle
# 아직 x

def dfs(level):
    # 현재 level 에서 선택할수 있는 x 좌표는 0 1 2
    if level == N :
        de = - 1
        return
    for x in range(N):
        if used[x] == 1 :
            continue
        used[x] = 1 # x좌표 사용(이후의 재귀호출에서 재사용 방지)
        dfs(level+1)
        used[x] = 0 # 원상복구
    return
    
for _ in range(10):
    N = int(input())
    dfs(N)

used = [0] * N # 0 1 2 의 사용 여부


