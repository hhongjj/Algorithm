# 1946 신입 사원
# 그리디 알고리즘, 정렬

import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    new = {}
    N = int(input())
    for j in range(N):
        a, b = map(int,input().split())
        new[a]=b
    new = sorted(new.items())
    cnt = 1
    x, y = new[0][0], new[0][1]
    for j in range(1, N):
        if x >= new[j][0] or y >= new[j][1]:
            cnt += 1
            y = new[j][1]
    print(cnt)
    

# 주어진 순위들을 dictionary로 받아와서 key로 정렬한 다음 튜플형태로 list로 바꾼다.
# list의 맨 앞 순위를 x, y로 받아온 후에 x, y보다 하나라도 작거나 같은 숫자가 있으면 cnt +=1 을 해준다
# 그리고 x의 값은 무조건 계속 1이지만, y는 보다 작은 수가 나타나면 바꾼다. 
# 예시를 들자면
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1
# 일 경우  정렬하면 
# 1 4
# 2 5
# 3 6
# 4 2
# 5 7
# 6 1
# 7 3 이렇게 되고 
# x y 값은
# 1 4
# 1 2
# 1 1 로 
# 1 4
# 4 2
# 6 1
# 만 신입사원이 된다.


# 문제 이해하는 것에서 힘들었다.
# 주어진것은 순위이다!! 1이 순위가 제일 높은 것!!
# 문제를 꼼꼼히 읽자...