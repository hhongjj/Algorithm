# G5 11509 풍선 맞추기
# https://www.acmicpc.net/problem/11509
# 그리디 알고리즘

import sys
input = sys.stdin.readline

# 화살이 해당 높이에 있으면 -1 하고 그 밑에 위치에 화살 하나 추가
# 없으면 그 밑에 위치에 화살 하나 추가
N = int(input())
H = list(map(int, input().split()))
cnt = 0
visited = [0]*1000001

for i in H:
    if visited[i]:
        visited[i-1] += 1
        visited[i] -= 1
    else:
        visited[i-1] += 1
        cnt += 1
print(cnt)


# 너무 많이 돈다!!
# 여러번 돌면서 지우는 것 nono
# while N > 0:
#     p = H[idx]
#     if not p:
#         idx += 1
#         continue
#     tmp_idx = idx
#     tmp = p - 1
#     while tmp in H[tmp_idx+1:]:
#         tmp_idx = H.index(tmp)
#         H[tmp_idx] = 0
#         tmp -= 1
#         N -= 1
#     H[idx] = 0
#     cnt += 1
#     idx += 1
#     N -= 1
# print(cnt)

# while H:
#     tmp = max(H)
#     idx = H.index(tmp)
#     p = tmp
#     while idx < len(H):
#         p -= 1
#         if p in H[idx:]:
#             idx = H.index(p)
#             H.remove(p)
#             if idx == len(H):
#                 break
#         else:
#             break
#     H.remove(tmp)
#     cnt += 1
# print(cnt)