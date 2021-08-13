# D3 10804 문자열의거울상

T = int(input())
for tc in range(1, T+1):
    word = input()
    print('#{}'.format(tc), end=' ')
    for i in range(len(word)-1, -1, -1):
        if word[i] == 'b':
            print('d', end='')
        elif word[i] == 'd':
            print('b', end='')
        elif word[i] == 'p':
            print('q', end='')
        else:
            print('p', end='')
    print('')