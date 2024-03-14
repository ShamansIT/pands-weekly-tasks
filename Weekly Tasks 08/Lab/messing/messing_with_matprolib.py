import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

plt.plot(xpoints, ypoints, label = "xsquared")
plt.plot(xpoints, xpoints, label = 'straight', color = "blue")
plt.legend()
#plt.savefig("lecture1.png")

random_points = np.random.randint(1, 1000, 100)
plt.scatter(xpoints, random_points , label = "random")

plt.show()

