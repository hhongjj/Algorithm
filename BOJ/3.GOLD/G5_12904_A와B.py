# G5 12904 A와 B
# https://www.acmicpc.net/problem/12904
# 구현, 문자열, 그리디 알고리즘

S = input()
T = input()

while len(S) < len(T):
    if T[-1] == 'A':
        T = T[:-1]       # 맨 뒤의 문자 제거
    else:
        T = T[:-1]
        T = T[::-1]      # 문자열 뒤집기

if S == T:
    print(1)
else:
    print(0)

# T를 문자를 제거하며 S로 바꾼다
# T의 맨 끝이 'A' 라면 A만 제거하고 'B' 라면 B를 제거하고 문자열을 뒤집는다.
# 길이가 같아지면 while 문을 나와 두 문자열을 비교하고 같으면 1 다르면 0을 출력
