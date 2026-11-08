def getMax(a):
    n = len(a)
    sparse = [[0]*(n+1) for i in range(1)]

    for i in range(1, n + 1):
        sparse[0][i] = a[i - 1]

    k = 0
    while 2 ** k <= n:
        sparse.append([0]*(n+1))
        for i in range(1, n + 1):
            j = min(n, i + 2**k)
            sparse[k + 1][i] = max(sparse[k][i], sparse[k][j])
        k += 1

    return sparse
    

N = int(input())
numbs = list(map(int, input().split()))
K = int(input())

pw = [0] * (N + 1)
pw[1] = 0
for i in range(2, N + 1):
    pw[i] = pw[i - 1]
    if not (i & (i - 1)):
        pw[i] += 1

sparse = getMax(numbs)

res = []
c = 0
while c < K:
    l, r = map(int, input().split())
    max2 = pw[r - l + 1]
    res.append(max(sparse[max2][l], sparse[max2][r - 2**max2 + 1]))
    c += 1

print(*res)
