import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [2, 4, 6, 8]

# Plot two lines
plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

# Add legend
plt.legend()

# Display the plot
plt.show()
