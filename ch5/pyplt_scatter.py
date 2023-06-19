import matplotlib.pyplot as plt
import numpy as np

x = np.array([3, 8, 9, 7, 5, 13, 4, 10, 2, 11, 9, 6, 5])
y = np.array([105, 92, 93, 87, 102, 98, 95, 89, 92, 79, 81, 91, 96])

plt.scatter(x, y)
plt.show()