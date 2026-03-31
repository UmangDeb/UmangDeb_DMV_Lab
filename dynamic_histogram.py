import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

def update(frame):
    ax.clear()  

    data = np.random.randn(200)

    ax.hist(data, bins=10, edgecolor='black')

    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Values")
    ax.set_ylabel("Frequency")

ani = FuncAnimation(fig, update, interval=1000)

plt.show()