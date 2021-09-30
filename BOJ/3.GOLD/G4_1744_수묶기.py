# G4 1744 수 묶기
# https://www.acmicpc.net/problem/1744
# 그리디 알고리즘, 정렬


def sum_num(lst):
    res = 0
    while lst:
        if len(lst) == 1:      # 숫자가 한개라면 더하기
            a = lst.pop()
            res += a
        else:
            a = lst.pop()
            b = lst.pop()
            if abs(a) > 1 and abs(b) > 1:    # 두 숫자의 절대값이 1 보다 크면 곱하기
                res += a * b
            else:                            # 숫자 중 한개라도 1보다 같거나 작으면
                if a < 0:                    # 음수일 경우는 곱하기
                    res += a * b
                else:                        # 양수일 경우는 더하기
                    res += a + b
    return res


N = int(input())
plus = []        # 양수
minus = []       # 0, 음수
for _ in range(N):
    x = int(input())
    if x > 0:
        plus.append(x)
    else:
        minus.append(x)

# 절대값이 큰 순으로 정렬
plus.sort()
minus.sort(reverse=True)

result = sum_num(plus) + sum_num(minus)
print(result)

# 양수와 0, 음수 로 나누어서 따로 계산한다.
# 양수는 무조건 큰 수부터 2개씩 묶어서 곱하고 더함.
# 음수도 절대값이 큰 수부터 2개씩 묶어서 곱해서 더한다.
# 0을 음수일 때 곱해줘서 음수를 상쇄시켜야하는데 그 부분을 생각을 못해서 시간이 좀 걸림.
