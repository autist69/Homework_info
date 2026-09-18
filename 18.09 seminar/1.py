def fib_number(n: int) -> int:
    if n in {0, 1}:
        return 1
    return fib_number(n - 1) + fib_number(n - 2)

n = int(input())
print(fib_number(n))
