import matplotlib.pyplot as plt
import numpy as np

sizes = [100, 500, 2000, 10000]

values1 = np.random.normal(0, 10, sizes[0])
values2 = np.random.normal(0, 10, sizes[1])
values3 = np.random.normal(0, 10, sizes[2])
values4 = np.random.normal(0, 10, sizes[3])

fig = plt.figure(figsize=(16, 9), dpi=100)

ax1 = fig.add_subplot(221, title="N = 100")
ax2 = fig.add_subplot(222, title="N = 500")
ax3 = fig.add_subplot(223, title="N = 2000")
ax4 = fig.add_subplot(224, title="N = 10000")

ax1.hist(values1, 50)
ax2.hist(values2, 50)
ax3.hist(values3, 50)
ax4.hist(values4, 50)

ax1.grid()
ax2.grid()
ax3.grid()
ax4.grid()

fig.suptitle("Normal distribution")

plt.show()
