# D2 12587 글자수

T = int(input())

for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    max_s = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                cnt += 1
            if max_s < cnt:
                max_s = cnt
    print('#{} {}'.format(tc, max_s))
