# D3 12646 할아버지가 남긴 땅
# .....xxxx
T = int(input())

def dfs(ground, visited):
    stack = []



for tc in range(1, T+1):
    H, W = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(H)]
    visited = [[0] * W for _ in range(H)]
