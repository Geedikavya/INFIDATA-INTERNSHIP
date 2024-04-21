import matplotlib.pyplot as plt # for visualization
import numpy as np  # for array operations

x = np.array([3,5,6,7])
y = np.array([7,8,6,5])

plt.plot(x, y)   # creating a plot
plt.xlabel("average pulse") #setting name for x-axis
plt.ylabel("calorie burn") #setting name for y-axis
plt.title("sports watch data")
plt.show()  # displaying the plot