# G4 18119 단어암기
# https://www.acmicpc.net/problem/18119
# 브루트포스 알고리즘, 비트마스킹
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
words = []
check = list([0]*(26) for _ in range(N))
for i in range(N):
    word = input().rstrip()
    for j in range(97, 123):
        if chr(j) in word:
            check[i][j-97] = 1
    
    words.append((word, sum(check[i])))
    

for _ in range(M):
    x, y = input().split()
    cnt = 0 
    for i in range(N):
        if y in words[i][0]:
            check[i][ord(y)-97] = ord(x) - 49
        if words[i][1] == sum(check[i]):
            cnt += 1

    print(cnt)


