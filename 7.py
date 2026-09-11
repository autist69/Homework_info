n = int(input()); numbers = list(map(int, input().split()))
for i in range(n):
    cnt_l, cnt_m = 0, 0
    for j in range(n):
        if j != i:
            if numbers[j] < numbers[i]:
                cnt_l += 1
            else:
                cnt_m += 1
    if cnt_l == cnt_m:
        print(numbers[i]); break