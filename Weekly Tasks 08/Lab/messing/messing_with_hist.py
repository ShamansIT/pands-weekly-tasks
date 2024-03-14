import numpy as np
import matplotlib.pyplot as plt

norm_data = np.random.normal(size = 1000)

"""
plt.hist(norm_data)
plt.show()
"""

fruits = np.array(['Apple', 'Orandge', 'Banana'])
numbers = np.array([23, 77, 500])

plt.pie(numbers, labels = fruits)
plt.legend()
plt.show()