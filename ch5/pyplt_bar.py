import matplotlib.pyplot as plt
import numpy as np

x = np.array(["E", "F", "G", "H"])
y = np.array([5, 2, 7, 4])

plt.bar(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bar Plot of x and y')
plt.show()
