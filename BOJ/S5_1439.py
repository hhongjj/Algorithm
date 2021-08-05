# 1439 뒤집기
# 그리디 알고리즘

import sys
input = sys.stdin.readline

a = 0
s = list(input().rstrip())

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        a += 1
    
if s[-1] != s[0]:
    a += 1
print(a//2)

# list에서 바로 뒤의 인덱스와 숫자가 다르면 +1을 해주고
# 맨 처음과 마지막이 숫자가 다르면 +1을 해준다.
# 그리고 숫자가 바뀌는게 11 00 11 이면 두번 인식이 되는 거이므로
# 나누기 2해줌