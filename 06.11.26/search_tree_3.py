N = int(input())
numbs = list(map(int, input().split()))
K = int(input())

nules = []
counter = [0] * (N + 1)
for i in range(1, N + 1):
    if numbs[i - 1] == 0:
        nules.append(i - 1)
        counter[i] = counter[i - 1] + 1
    else:
        counter[i] = counter[i - 1]

res = []
c = 0
while c < K:
    l, r, k = map(int, input().split())
    indl = counter[l]
    indr = counter[r]
    if l - 1 in nules:
        if indl + k - 1 <= len(nules) and indr - indl + 1 >= k:
            res.append(nules[indl + k - 2])
        else:
            res.append(-1)
    else:
        if indl <= len(nules) and indr - indl >= k:
            res.append(nules[indl + k - 1])
        else:
            res.append(-1)
    c += 1

print(*res)
