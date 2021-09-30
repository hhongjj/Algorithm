# D3 1240 단순 2진 암호코드

pat = {'0001101': 0,
       '0011001': 1,
       '0010011': 2,
       '0111101': 3,
       '0100011': 4,
       '0110001': 5,
       '0101111': 6,
       '0111011': 7,
       '0110111': 8,
       '0001011': 9,
       }

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    check = 0
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                start = (i, j)
                check = 1
                break
        if check:
            break
    lst = arr[start[0]][start[1]-55:start[1]+1]
    stack = []
    for i in range(0, len(lst), 7):
        stack.append(lst[i:i+7])
    odd = 0
    result = 0
    for i in range(len(stack)):
        if i % 2 == 0:
            odd += pat[stack[i]]
        else:
            result += pat[stack[i]]
    if (result + odd * 3) % 10 == 0:
        print('#{} {}'.format(tc, result + odd))
    else:
        print('#{} 0'.format(tc))



