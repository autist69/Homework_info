"""I asked the neural network how to work with functions from the `random` library."""

import numpy as np
import random

from pathlib import Path

n = int(input("Enter the number of points: "))
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
lines = []
for i in range(n):
    x = random.uniform(0, 100)
    y_best = a*x + b
    error = random.gauss(0, 1.0)
    y = y_best + error
    lines.append([x, y])

with Path("information.txt").open("w") as f:
    for line in lines:
        f.write(f"{line[0]} {line[1]}\n")

with Path("information.txt").open("r") as f:
    lines = f.readlines()
    length = len(lines)
    all_x = np.full((1, length), 0, dtype="float32")
    all_y = np.full((1, length), 0, dtype="float32")

    for i in range(length):
        lines[i] = lines[i].strip()
        x, y = map(float, lines[i].split())
        all_x[0, i] = x
        all_y[0, i] = y

    total_y = np.sum(all_y)
    total_x = np.sum(all_x)
    y_ = total_y / length
    x_ = total_x / length
    xy = np.sum(all_x * all_y) / length
    x_y = y_ * x_
    _x2_ = np.sum(all_x**2) / length
    x_2 = (total_x/length) ** 2
    a = (xy-x_y) / (_x2_-x_2)
    b = y_ - a*x_

    print(round(a, 4), round(b, 4))
