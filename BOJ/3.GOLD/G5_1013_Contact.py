# G5 1013 Contact
# https://www.acmicpc.net/problem/1013
# 문자열, 정규 표현식
# 참고 https://wikidocs.net/4308#match

import re
import sys
input = sys.stdin.readline

T = int(input())
p = re.compile('(100+1+|01)+')
for _ in range(T):
    signal = input().rstrip()
    m = p.fullmatch(signal)
    if m:
        print("YES")
    else:
        print("NO")

