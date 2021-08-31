# G5 4811 알약
# 다이나믹 프로그래밍

def pill(w, h):
    global dp
    if not h and not w:
        return 1
    if dp[w][h] != -1:
        return dp[w][h]
    if w > 0:
        dp[w][h] += pill(w-1, h+1)
    if h > 0:
        dp[w][h] += pill(w, h-1)

    return dp[w][h]



while 1:
    N = int(input())
    if not N:
        break
    dp = [[-1] * 31 for _ in range(31)]
    pill(N, 0)
    print(dp[-1][-1])

    # res = pill(N)
    # print(res)


# 카탈란 수 (1,2,5,14,42,132,...)
