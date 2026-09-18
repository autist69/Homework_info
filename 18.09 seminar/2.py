def simple_numbers(x: int) -> list:
    sim_num = []
    divider = 2
    while x > 1:
        if divider * divider > x:
            sim_num.append(x)
            x = 1
        elif x % divider == 0:
            sim_num.append(divider)
            x //= divider
            divider = 2
        else:
            divider += 1
    return sim_num

n = int(input())
print(*simple_numbers(n))
