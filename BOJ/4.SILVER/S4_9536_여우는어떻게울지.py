# S4 9536 여우는 어떻게 울지?
# https://www.acmicpc.net/problem/9536
# 문자열, 파싱

T = int(input())
voice = input().split(' ')
sound = []

while 1:
    animal = input().split(' goes ')  # 'goes'를 기준으로 잘라서 입력받는다.

    if 'what does the fox say?' in animal:  # 질문이 주어지면 break
        break
    else:     # 동물의 울음 소리를 저장한다.
        sound.append(animal[1])


for v in voice:
    if v not in sound:    # 다른 동물의 울음소리가 아니라면 print
        print(v, end=' ')

