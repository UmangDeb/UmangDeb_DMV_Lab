import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 17, 20]

fig, ax = plt.subplots()

scatter = ax.scatter(x, y)

ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Animated Scatter Plot with Grid")
ax.grid(True)
ax.set_ylim(0, 30)

def update(frame):
    new_y = [random.randint(5, 25) for _ in y]  # change Y values
    scatter.set_offsets(list(zip(x, new_y)))    # update points

ani = FuncAnimation(fig, update, interval=1000)

plt.show()