A = list(map(int, input().split()))
for i in range(len(A)):
    f = True; j, cnt = 0, 0
    while f and j < len(A):
        if A[i] == A[j]:
            cnt += 1; j += 1
        else:
            j += 1
        if cnt > 1:
            f = False
    if f:
        print(A[i], end = " ")