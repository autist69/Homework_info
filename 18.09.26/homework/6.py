from pathlib import Path

import numpy as np

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

    print(round(a, 5), round(b, 5))
