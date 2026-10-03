import math

r, a = map(int, input().split())

length = 2 * math.pi * r
circle_s = math.pi * r**2
square_s = a ** 2

print(f"""Длина окружности равно {length:.2f}.
       Площадь круга составляет {100 * (circle_s/square_s):.2f}% от площади квадрата""")
