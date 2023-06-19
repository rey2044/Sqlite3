import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram of Randomly Generated Data')
plt.show()
