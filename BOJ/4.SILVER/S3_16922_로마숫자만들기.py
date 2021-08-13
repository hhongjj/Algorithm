# S3 16922 로마 숫자 만들기
# 수학, 구현, 브루트포스 알고리즘, 조합론, 백트래킹
import sys
input = sys.stdin.readline

N = int(input())
arr = [1, 5, 10, 50]
result = []
sum_l = []
def Rome(idx, sum_l: list):
    global N
    if len(sum_l) == N:
        result.append(sum(sum_l))
        return
    for i in range(idx, len(arr)):
        sum_l.append(arr[i])
        Rome(i, sum_l)                # 중복 가능함
        sum_l.pop()

Rome(0, sum_l)
result = set(result)
print(len(result))

