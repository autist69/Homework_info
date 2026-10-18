from itertools import combinations

class Vector:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, str):
            numbs = x.strip("{} ").split(",")
            x, y, z = map(float, numbs)

        assert isinstance(x, (int, float)), "Неправильный формат данных"
        assert isinstance(y, (int, float)), "Неправильный формат данных"
        assert isinstance(z, (int, float)), "Неправильный формат данных"

        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __abs__(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return "Неправильный формат данных"

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        return "Неправильный формат данных"

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return Vector(self.x * other.x + self.y * other.y + self.z * other.z)
        return "Неправильный формат данных"

fl = int(input("Выбирете операцию (1 или 2): "))
n = int(input("Введите количество точек: "))
points = [0] * n

for i in range(n):
    A = Vector(input())
    points[i] = A

if fl - 1:
    max_s = 0
    for p1, p2, p3 in combinations(points, 3):

        v1 = p2 - p1
        v2 = p3 - p1
        cx = v1.y * v2.z - v1.z * v2.y
        cy = v1.z * v2.x - v1.x * v2.z
        cz = v1.x * v2.y - v1.y * v2.x

        S = (cx**2 + cy**2 + cz**2)**0.5 / 2

        max_s = max(max_s, S)

    print(max_s)

else:
    all_sum = Vector(0, 0, 0)
    if n == 0:
        print(all_sum)
    else:
        for v in points:
            all_sum = all_sum + v

        print(all_sum * (1/n))
