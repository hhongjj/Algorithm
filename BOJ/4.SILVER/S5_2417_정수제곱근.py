# S5 2417 정수제곱근
# 수학, 이분 탐색

n = int(input())

if n**0.5 % 1 != 0:
    q = int(n**0.5)+1
    print(q)
else:
    q = int(n ** 0.5)
    print(q)


# 이분탐색
s, e = 1, n // 2
mid = (s + e) // 2
while s <= e:
    mid = (s + e) // 2
    if mid ** 2 == n:
        break
    elif mid ** 2 > n:
        e = mid - 1
    else:
        s = mid + 1


if mid ** 2 >= n:
    print(mid)
else:
    print(mid+1)
