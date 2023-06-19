import numpy as np
import matplotlib.pyplot as plt

x = np.array([6,7,8])
y = np.array([1,5,6])

#title function
plt.title("Health Report")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y)
plt.grid(plt.grid(color = 'green', linestyle = '--', linewidth = 0.5))
plt.show()