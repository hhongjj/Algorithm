#1209 [S/W 문제해결 기본] 2일차 - Sum
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=1209&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

for i in range(10):
    T = int(input())
    arr1 = []                   # 오른쪽으로 내려가는 대각선 리스트
    arr2 = []                   # 왼쪽으로 내려가는 대각선 리스트
    sum_max = 0
    arr = [0]*100               # 세로로 더할 리스트
    for j in range(100):
        num = list(map(int,input().split()))
        arr = [arr] + [num]                      # 이전까지의 세로로 더한 리스트와 새로 들어오는 리스트를 2차원 리스트로 더함.
        arr = list(map(sum, zip(*arr)))          # zip을 이용해 세로로 다 더한 리스트 만들기 
        sum_max = max(sum(num), sum_max)
        arr1.append(num[j])
        arr2.append(num[-(j+1)])
    print(f'#{T} {max(sum(arr1),sum(arr2),sum_max, max(arr))}')




# arr = [1,2,3,4,5,6]
# rrr = [3,4,5,6,7,8]
# arr = [arr] + [rrr]
# print(arr)
# print(list(map(sum, zip(*arr))))
# zip함수를 이용해 반복문 돌리지 않고 리스트 인덱스끼리 더하기!