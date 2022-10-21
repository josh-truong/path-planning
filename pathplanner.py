import numpy as np
import matplotlib.pyplot as plt

from astar import Astar
from approxspace import ApproxSpace

map = np.load('map.npy')
config_map = ApproxSpace(map, rectangle=(11.99, 11.99))
path = Astar(config_map, start=(90, 25), end=(225,255))

fig, ax = plt.subplots(1)
for x, y in path:
    circle = plt.Circle((x, y), 6, color='r', alpha=0.1)
    ax.add_patch(circle)
ax.imshow(config_map)
ax.imshow(map, alpha=0.5)
plt.show()