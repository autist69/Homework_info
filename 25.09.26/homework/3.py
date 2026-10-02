import matplotlib.pyplot as plt
import pandas as pd

iris_data = pd.read_csv("iris_data.csv")

sl = list(iris_data["SepalLengthCm"])
sw = list(iris_data["SepalWidthCm"])
pl = list(iris_data["PetalLengthCm"])
pw = list(iris_data["PetalWidthCm"])

fig = plt.figure(figsize = (16, 10))

ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax6 = fig.add_subplot(326)

ax1.scatter(sl, sw, "b^")
ax2.scatter(sl, pl, "b^")
ax3.scatter(sl, pw, "b^")
ax4.scatter(sw, pl, "b^")
ax5.scatter(sw, pw, "b^")
ax6.scatter(pl, pw, "b^")

plt.show()
