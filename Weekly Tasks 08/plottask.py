# Weekly Task 8
# Created by Serhii Spitsyn

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
mean = 5
dev = 2
values = np.random.normal(mean, dev, 1000)

# Plot histogram
plt.hist(values, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')

#Add labels and titles
plt.xlabel('x')
plt.ylabel('Destiny')
plt.title('Histogram of Normal Distribution')
plt.grid(True)
plt.legend(['Normal Distribution'], loc='upper right')

# Show
plt.show()

# Plot function h(x) = x^3
x = np.linspace(0, 10 , 1000)
y = x ** 3
plt.plot(x, y, 'r-', linewidth = 1.5)

# Add labels and titles
plt.xlabel('x')
plt.ylabel('Function value')
plt.title('Histogram of Function h(x) = x^3')
plt.grid(True)
plt.legend(['h(x) = x^3'], loc='upper right')

# Show
plt.show()
