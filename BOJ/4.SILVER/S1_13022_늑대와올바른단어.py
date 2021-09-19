# S1 13022 늑대의 올바른 단어
# https://www.acmicpc.net/problem/13022
# 구현, 문자열, 파싱


word = input()
run = 1
idx = 0
while idx < len(word) and run:
    cnt = 0
    if 'w' == word[idx]:
        idx += 1
        cnt += 1
        while 1:
            if 'w' == word[idx]:
                cnt += 1
                idx += 1
            else:
                break
    else:
        run = 0
        break
    if idx >= len(word)-2:
        break
    check = cnt
    if 'o' == word[idx]:
        check -= 1
        idx += 1
        while check and idx < len(word):
            if 'o' == word[idx]:
                check -= 1
                idx += 1
            else:
                run = 0
                break
    else:
        run = 0
        break
    if not run or check:
        break

    if idx >= len(word)-2:
        break
    check = cnt
    if 'l' == word[idx]:
        check -= 1
        idx += 1
        while check and idx < len(word):
            if 'l' == word[idx]:
                check -= 1
                idx += 1
            else:
                run = 0
                break
    else:
        run = 0
        break
    if not run or check:
        break

    if idx >= len(word)-1:
        break
    check = cnt
    if 'f' == word[idx]:
        check -= 1
        idx += 1
        while check and idx < len(word):
            if 'f' == word[idx]:
                check -= 1
                idx += 1
            else:
                run = 0
                break
    else:
        run = 0
        break
    if not run or check:
        break

if run and not check:
    print(1)
else:
    print(0)



