import matplotlib.pyplot as plt
import numpy as np

# Coordinates of the places
places = {'Place 1': (9, 4), 'Place 2': (4, 6), 'Place 3': (4, 4), 'Place 4': (3, 4), 'Place 5': (4, 8)}

# Tour order based on the solution provided
tour_order = ['Place 1', 'Place 3', 'Place 4', 'Place 2', 'Place 5', 'Place 1']

# Extracting coordinates in the order of the tour
x_coords = [places[place][0] for place in tour_order]
y_coords = [places[place][1] for place in tour_order]

# Visualizing the tour
plt.figure(figsize=(10, 8))
plt.plot(x_coords, y_coords, '-o', mfc='red')  # Path and points
# Mark each move with an arrow
for i in range(len(x_coords)-1):
    plt.annotate('', xy=(x_coords[i + 1], y_coords[i + 1]), xytext=(x_coords[i], y_coords[i]),
                 arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate places
for i, place in enumerate(tour_order):
    if i < len(tour_order) - 1:  # Avoid duplicating the start/end annotation
        plt.text(x_coords[i], y_coords[i], f"{place}", fontsize=12, ha='right')

plt.title('Robot Tour Visualization')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.axis('equal')
plt.show()