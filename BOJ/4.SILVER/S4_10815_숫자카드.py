# S4 10815 숫자 카드
# 정렬, 이분 탐색

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))
M = int(input())
sang = list(map(int, input().split()))

card = sorted(card)


def bin(start, last, word):
    mid = (start+last) // 2
    if last - start <= 1:
        if card[last] == word or card[start] == word:
            print(1, end=' ')
        else:
            print(0, end=' ')
        return
    elif card[mid] == word:
        print(1, end=' ')
        return
    elif card[mid] > word:
        last = mid - 1
        bin(start, last, word)
    else:
        start = mid + 1
        bin(start, last, word)

for i in sang:
    bin(0, N-1, i)