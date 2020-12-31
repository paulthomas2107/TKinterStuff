from tkinter import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


root = Tk()
root.title("Map Plotting...")
root.geometry('400x200')


def graph():

    house_prices = np.random.normal(200000, 25000, 5000)
    # plt.hist(house_prices, 50)
    plt.polar(house_prices)
    plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


my_button = Button(root, text="Press for graph", command=graph)
my_button.pack()

"""
n_radii = 8
n_angles = 36

# Make radii and angles spaces (radius r=0 omitted to eliminate duplication).
radii = np.linspace(0.125, 1.0, n_radii)
angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]

# Convert polar (radii, angles) coords to cartesian (x, y) coords.
# (0, 0) is manually added at this stage,  so there will be no duplicate
# points in the (x, y) plane.
x = np.append(0, (radii*np.cos(angles)).flatten())
y = np.append(0, (radii*np.sin(angles)).flatten())

# Compute z to make the pringle surface.
z = np.sin(-x*y)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()
"""

root.mainloop()
