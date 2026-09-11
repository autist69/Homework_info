# 1

A = list(map(int, input().split())); B = [False] * A[0]
for i in range (1, A[0]):
    B[A[i] - 1] = True
for i in range (A[0]):
    if B[i] == False:
        print(i + 1); break