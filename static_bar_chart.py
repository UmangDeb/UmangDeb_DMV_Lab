import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [10, 25, 15, 30, 20]

plt.bar(categories, values)

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Simple Bar Chart")

plt.show()