def triangle_down(n: int, start_n: int, symb: str) -> None:
    if n == start_n:
        return

    print(n * symb)

    triangle_down(n + 1, start_n, symb)

def triangle_up(n: int, symb: str) -> None:
    if n == 0:
        return

    print(n * symb)

    triangle_up(n - 1, symb)

def triangle(n: int, symb: str) -> None:
    if n % 2 == 0:
        middle_n = n // 2
        triangle_down(1, middle_n + 1, symb)
        triangle_up(middle_n, symb)
    else:
        middle_n = n // 2 + 1
        triangle_down(1, middle_n + 1, symb)
        triangle_up(middle_n - 1, symb)

n, symb = map(str, input().split())
triangle(int(n), symb)
