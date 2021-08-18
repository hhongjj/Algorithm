#E D2_회문
# 다시해보기
def is_palindrome(str_):
    n = len(str_)
    for i in range(n):
        if str_[i] != str_[n-1-i]:
            return 0
    return 1

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())   # N x N 2차원 리스트 / M 은 palindrome 길이
    MAP = []
    for y in range(N):
        MAP.append(input())
    # 가로 회문 검사
    ans = ""
    for y in range(N):
        for x in range(N-M + 1):
            temp_str = MAP[y][x:x+M]
            ret = is_palindrome(temp_str)   # O(M)
            if ret == 1:
                ans = temp_str

    # 세로 회문 검사
    for x in range(N):
        for y in range(N-M + 1):
            temp_str = ""
            # O(M)
            for i in range(y, y + M):
                temp_str += MAP[i][x]
            # O(M)
            ret = is_palindrome(temp_str)
            if ret == 1:
                ans = temp_str

    print("#{} {}".format(tc, ans))
