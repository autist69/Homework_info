import matplotlib.pyplot as plt
import pandas as pd

iris_data = pd.read_csv("iris_data.csv")

types = list(iris_data["Species"])
length = list(iris_data["PetalLengthCm"])

counter = len(types)

flow_number = {}
for name in types:
    if name not in flow_number:
        flow_number[name] = 1
    else:
        flow_number[name] += 1

sizes = [1.2, 1.5]
petal_len = [0] * 3
for numb in length:
    if numb <= sizes[0]:
        petal_len[0] += 1
    elif sizes[0] < numb <= sizes[1]:
        petal_len[1] += 1
    else:
        petal_len[2] += 1

fig = plt.figure(figsize = (12, 6))

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.pie(flow_number.values(), labels=flow_number.keys())
ax2.pie(petal_len, labels=["<= 1.2", "1.2 < and <= 1.5", "> 1.5"])

ax1.set_title("Types of irises, %")
ax2.set_title("Syzes fo petals, %")

fig.suptitle("Flowers' statistic", fontsize=16)

plt.show()
