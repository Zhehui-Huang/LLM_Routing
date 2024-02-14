import matplotlib.pyplot as plt
import numpy as np

# Define the places
places = {'Place 1': np.array([9, 4]),
          'Place 2': np.array([4, 6]),
          'Place 3': np.array([4, 4]),
          'Place 4': np.array([3, 4]),
          'Place 5': np.array([4, 8])}

fig, ax = plt.subplots()
# Plot each point and add annotations for each place.
for place, coords in places.items():
    ax.plot(*coords, 'o', label=place)
    ax.text(coords[0], coords[1], f' {place}', verticalalignment='bottom')

# Define the tour
tour = ['Place 1', 'Place 3', 'Place 4', 'Place 2', 'Place 5', 'Place 1']

# Draw arrows between places in the tour
for i in range(len(tour)-1):
    start_place, end_place = tour[i], tour[i+1]
    ax.annotate("",
                xy=places[end_place], xycoords='data',
                xytext=places[start_place], textcoords='data',
                arrowprops=dict(arrowstyle="->", color="r", lw=1.5),
                )

plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Shortest Path for Robot Tour')
plt.grid(True)
plt.axis('equal')
plt.show()