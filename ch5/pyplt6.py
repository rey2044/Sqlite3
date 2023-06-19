import matplotlib.pyplot as plt

# Create two subplots
plt.subplot(1, 2, 1)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.subplot(1, 2, 2)
plt.plot([1, 2, 3, 4], [1, 8, 27, 64])

# Display the subplots
plt.show()
