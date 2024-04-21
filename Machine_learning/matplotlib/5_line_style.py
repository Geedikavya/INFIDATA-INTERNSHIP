import matplotlib.pyplot as plt # for visualization
import numpy as np  # for array operations

x = np.array([0,6])
ypoints = np.array([0,10])

plt.plot( ypoints, linestyle="dotted", color='red')   # linestyle
plt.show()  # displaying the plot

plt.plot( ypoints, linestyle="dashed", linewidth=5, color='#ffcee0')
plt.show()  # displaying the plot

plt.plot( ypoints, ls="dashdot", lw=10)
plt.show()  # displaying the plot

plt.plot( ypoints, ls="solid")   # linestyle
plt.show()  # displaying the plot