# 1206 View

for i in range(1, 11):
    n = int(input())
    num_list = list(map(int, input().split()))
    cnt = 0
    for j in range(2,n-2):
        h = num_list[j]
        if num_list[j-2] < h and num_list[j-1] < h and num_list[j+1] < h and num_list[j+2] < h:
            cnt += h - max(num_list[j-2], num_list[j-1], num_list[j+1], num_list[j+2])
        
    print(f'#{i} {cnt}')