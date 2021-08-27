# G5 12865 평범한 배낭
# 다이나믹 프로그래밍, 배낭 문제


def knapsack():
    pack = []
    for i in range(N + 1):
        pack.append([])
        for c in range(K + 1):
            if not i or not c:
                pack[i].append(0)
            elif cargo[i-1][0] <= c:     # 무게가 c보다 작다면 pack[i]에 가치합의 max값을 추가
                pack[i].append(max(cargo[i-1][1] + pack[i-1][c-cargo[i-1][0]], pack[i-1][c]))
                #  pack[i-1][K-cargo[i-1][0] : 무게 c에서 인덱스 i-1의 무게를 빼고 남은 무게에 해당되는 곳의 가치값을 더함 vs 배낭 갯수는 하나 적어도 최대값일 수도 있으니 비교
            else:
                pack[i].append(pack[i-1][c])
    return pack[-1][-1]


N, K = map(int, input().split())
cargo = []
for _ in range(N):
    W, V = map(int, input().split())
    cargo.append((W, V))

res = knapsack()
print(res)



# pack의 행은 물품의 수, 열은 무게이다.
# 그 위치까지의 물품의 개수와 배낭의 용량에 따른 최댓값.
# 타뷸레이션 방식
# pack = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 13, 13], [0, 0, 0, 0, 8, 8, 13, 13], [0, 0, 0, 14, 14, 14, 14, 14], [0, 0, 0, 14, 14, 14, 14, 14]]