# S1 2343 기타레슨
# 이분 탐색

N, M = map(int, input().split())
lst = list(map(int, input().split()))

st = max(lst)
end = sum(lst)
ans = sum(lst)
while st <= end:
    cnt = 0
    mid = (st + end) // 2
    lesson = 0
    for i in range(N):
        # 더했을때 mid 보다 작거나 같으면 더함
        if lesson + lst[i] <= mid:
            lesson += lst[i]
        else:
            lesson = lst[i]
            cnt += 1
    if lesson:
        cnt += 1
    if cnt <= M:
        end = mid - 1
        ans = min(mid, ans)
    else:
        st = mid + 1

print(ans)

# 엄청 틀리다가 st를 max(lst)로 바꾸니 해결.. 범위가 엄청 중요하다 처음에는 평균으로 잡았었다.
# 배열 중 최대값을 start로 잡고, 총 합을 end로 잡는다.
# 누적합을 lesson 으로 두고 누적합이 mid보다 크면 count 하고 lesson 값을 바꿔준다.
# 마지막에 lesson값이 있다면 한개 더 카운트 해줌
# 만족하는 최소값을 찾아야하므로 ans에 mid와 비교를 해서 최소값을 담아둔다.