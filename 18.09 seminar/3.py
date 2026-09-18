def evcklid_algoritm(a: int, b: int) -> list:
    if b == 0:
        return 1, 0, a
    x, y, d = evcklid_algoritm(b, a % b)
    x, y = y, x - (a // b) * y
    return x, y, d

a, b = map(int, input().split())
print(*evcklid_algoritm(a, b))
