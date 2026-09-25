import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([2.5, 15.0, 22.2, 46.4, 73.8, 79.6, 83.4, 95.5, 103.3, 105.2])
y1 = np.array([12.0, 72.0, 108.0, 228.0, 364.0, 392.0, 408.0, 468.0, 508.0, 516.0])

x2 = np.array([7.8, 19.3, 21.2, 39.0, 65.4, 80.4, 89.6, 91.0, 105.5, 107.7])
y2 = np.array([24, 56, 64, 116, 192, 236, 264, 268, 312, 320])

x3 = np.array([24.1, 28.6, 43.9, 60.5, 70.4, 102.5, 107.6, 111.5, 141.2, 177.6])
y3 = np.array([48, 56, 88, 120, 140, 204, 216, 220, 280, 352])

plt.figure(figsize=(12, 9), dpi=100)

plt.plot([0.0, 110], [0.0, 540], "r", label="L = 50 sm", zorder=2)
plt.plot([0.0, 140], [0.0, 410], "y", label="L = 30 sm", zorder=2)
plt.plot([0.0, 180], [0.0, 355], "g", label="L = 20 sm", zorder=2)

plt.scatter(x1, y1, color="k", marker="x", zorder=3)
plt.scatter(x2, y2, color="k", marker="*", zorder=3)
plt.scatter(x3, y3, color="k", marker="^", zorder=3)

plt.legend()
plt.title("VAC of nichrome wire")

X = [i for i in range(0, 201, 20)]
Y = [i for i in range(0, 501, 100)]

plt.xticks(X)
plt.yticks(Y)
plt.grid()

plt.show()
