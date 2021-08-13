# D3 1213 [S/W 문제해결 기본] 3일차 - String

def find_word(start_idx, word_len):
    if start_idx + word_len - 1 >= len(sen):
        return 0
    for i in range(word_len):
        if sen[start_idx + i] != word[i]:
            return 0
    return 1

for tc in range(10):
    T = int(input())
    word = input()
    sen = input()
    cnt = 0
    for i in range(len(sen)):
        ret = find_word(i, len(word))
        if ret == 1:
            cnt += 1
    print('#{} {}'.format(T, cnt))