#D2 2005 파스칼의삼각형

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc))
    result = []
    for i in range(N):
        if i > 1:
            temp = [1]
            for j in range(len(result) - 1):
                temp.append(result[j] + result[j + 1])
            result = temp
        result.append(1)
        print(' '.join(map(str, result)))
