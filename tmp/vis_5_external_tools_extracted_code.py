import matplotlib.pyplot as plt

# Define the tour and its locations
tour = ['P1', 'P3', 'P4', 'P2', 'P5', 'P1']
locations = {'P1': (9, 4), 'P2': (4, 6), 'P3': (4, 4), 'P4': (3, 4), 'P5': (4, 8)}

# Extract the coordinates for plotting
x_coords = [locations[place][0] for place in tour]
y_coords = [locations[place][1] for place in tour]

# Plotting the tour
plt.figure(figsize=(10, 6))
plt.plot(x_coords, y_coords, marker='o')

# Annotating the places
for place, (x, y) in locations.items():
    plt.text(x + 0.1, y + 0.1, place)

# Drawing arrows
for i in range(len(x_coords) - 1):
    plt.arrow(x_coords[i], y_coords[i], x_coords[i + 1] - x_coords[i], y_coords[i + 1] - y_coords[i], 
              head_width=0.1, head_length=0.2, length_includes_head=True)

plt.title('Robot Tour Visualization')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.axis('equal')
plt.show()