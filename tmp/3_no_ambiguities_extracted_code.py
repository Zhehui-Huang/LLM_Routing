import matplotlib.pyplot as plt
import numpy as np

# Points location
points = {'Place 1': (9, 4), 'Place 3': (4, 4), 'Place 4': (3, 4), 'Place 2': (4, 6), 'Place 5': (4, 8), 'Return to Place 1': (9, 4)}

# Extracting x and y coordinates for plotting
x, y = zip(*points.values())

# Plot settings
fig, ax = plt.subplots()
ax.plot(x, y, 'o-', mfc='r', mec='k') # Places and paths between them
ax.set_aspect('equal')

# Annotate places
for i, txt in enumerate(points.keys()):
    ax.annotate(txt, (x[i], y[i]))

# Draw arrows
for i in range(len(x)-1):
    plt.arrow(x[i], y[i], x[i+1]-x[i], y[i+1]-y[i], head_width=0.2, length_includes_head=True)

plt.show()