# D3 4406 모음이 보이지 않는 사람

def vowel(word):
    for i in word:
        if i not in ['a', 'e', 'i', 'o', 'u']:
            print(i, end='')
    return

T = int(input())

for tc in range(1, T+1):
    word = input()
    print('#{}'.format(tc), end=' ')
    vowel(word)
    print('')
