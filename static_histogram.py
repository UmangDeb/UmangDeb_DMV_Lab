import matplotlib.pyplot as plt

data = [12, 15, 13, 17, 18, 19, 21, 22, 22, 23, 25, 27, 29, 30, 30]

plt.hist(data, bins=5, edgecolor="black")

plt.title("Static Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()