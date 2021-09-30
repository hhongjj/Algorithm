# D5 1242 암호코드 스캔
# 같은 라인에 암호코드가 2개 있는 경우도 있음
# 라인에 한개만 있는 줄 알고 품...
pat = {
        '0001101': 0,
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


def is_valid(data, scale):
    data = data[::scale]  # 이용해서
    for i in range(0, len(data), 7):
        if data[i:i + 7] in pat:
            continue
        else:
            return -1
    return 1
    # data 가 올바른 코드인지 검증하기


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lines = set()  # 한 라인을 통째로 2진수로 바꾼 값들을 add
    for _ in range(N):
        temp = input().strip('0')  # 0 제거
        if temp == '':
            continue
        # 한 라인을 통째로 2진수로 바꿔서 set 에 등록
        # 1DB176C588D26EC00000000196EBC5A316C578 -> 이렇게 한라인에 있을 수 있다.
        line = bin(int(temp, 16))[2:].rstrip('0')
        lines.add(line)

    codes = set()  # 암호를 풀어서 넣기
    for line in lines:
        # line 오른쪽에 있는 0 은 제거된 상태 , / 7bit 1개 숫자 or 14bit 가 1개 숫자 or 21bit 1개 숫자.......
        scale = 1
        while line:
            ret = 1
            tmp = line[-56 * scale:]
            if len(tmp) != 56*scale:
                tmp = tmp.zfill(56*scale)
            ret = is_valid(tmp, scale)
            if ret == -1:
                # line = line[:-56 * scale].rstrip('0')
                scale += 1
            else:
                codes.add(tmp)
                break
            break

    ans = 0
    codes = list(codes)
    for j in range(len(codes)):
        stack = []
        for i in range(0, len(codes[j]), 7):
            stack.append(codes[j][i:i + 7])
        odd = 0
        result = 0
        for i in range(len(stack)):
            if i % 2 == 0:
                odd += pat[stack[i]]
            else:
                result += pat[stack[i]]

        if (result + odd * 3) % 10 == 0:
            ans += result + odd

    print('#{} {}'.format(tc, ans))
