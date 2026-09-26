import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

iris_data = pd.read_csv("iris_data.csv")

sl = list(iris_data["SepalLengthCm"])
sw = list(iris_data["SepalWidthCm"])
pl = list(iris_data["PetalLengthCm"])
pw = list(iris_data["PetalWidthCm"])

fig = plt.figure(figsize = (16, 10))

ax1 = fig.add_subplot(231, title="Sepal length ~ sepal width, (cm : cm)")
ax2 = fig.add_subplot(232, title="Sepal length ~ petal length, (cm : cm)")
ax3 = fig.add_subplot(233, title="Sepal length ~ petal width, (cm : cm)")
ax4 = fig.add_subplot(234, title="Sepal width ~ petal length, (cm : cm)")
ax5 = fig.add_subplot(235, title="Sepal width ~ petal width, (cm : cm)")
ax6 = fig.add_subplot(236, title="Petal length ~ petal width, (cm : cm)")

ax1.scatter(sl, sw, marker="^")
ax2.scatter(sl, pl, marker="^")
ax3.scatter(sl, pw, marker="^")
ax4.scatter(sw, pl, marker="^")
ax5.scatter(sw, pw, marker="^")
ax6.scatter(pl, pw, marker="^")

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()
ax5.grid()
ax6.grid()

z2 = np.polyfit(sl, pl, 1)
p2 = np.poly1d(z2)
x2_app = [4.0, 8.0]

z3 = np.polyfit(sl, pw, 1)
p3 = np.poly1d(z3)
x3_app = [4.0, 8.0]

z6 = np.polyfit(pl, pw, 1)
p6 = np.poly1d(z6)
x6_app = [0.5, 7.5]

ax2.plot(x2_app, p2(x2_app), "r--")
ax3.plot(x3_app, p3(x3_app), "r--")
ax6.plot(x6_app, p6(x6_app), "r--")

fig.suptitle("Parameter dependencies", fontsize=20)

plt.show()
