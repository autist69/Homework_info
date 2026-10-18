def maxel(numbs:list, n:int, i:int)->None:
    m = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and numbs[m] < numbs[left]:
        m = left

    if right < n and numbs[m] < numbs[right]:
        m = right

    if m != i:
        numbs[i], numbs[m] = numbs[m], numbs[i]
        maxel(numbs, n, m)

def maxdown(numbs:list, n:int)->None:
    for i in range(n // 2 - 1, -1, -1):
        maxel(numbs, n, i)

    for i in range(n - 1, 0, -1):
        numbs[i], numbs[0] = numbs[0], numbs[i]
        maxel(numbs, i, 0)

numbs = list(map(int, input().split()))
n = len(numbs)

maxdown(numbs, n)

print(*numbs)
