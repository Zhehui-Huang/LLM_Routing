from itertools import permutations
import math

# Points setup
points = {'Place 1': (9, 4), 'Place 2': (4, 6), 'Place 3': (4, 4), 'Place 4': (3, 4), 'Place 5': (4, 8)}

# Function to calculate distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate all permutations of places to visit (excluding start point)
perm = permutations(['Place 2', 'Place 3', 'Place 4', 'Place 5'])

# Find the shortest path
shortest_distance = None
best_path = None
start_point = 'Place 1'

for path in perm:
    # Calculate distance for this permutation
    curr_distance = distance(points[start_point], points[path[0]])
    for i in range(len(path) - 1):
        curr_distance += distance(points[path[i]], points[path[i + 1]])
    curr_distance += distance(points[path[-1]], points[start_point])  # Return to start

    if shortest_distance is None or curr_distance < shortest_distance:
        shortest_distance = curr_distance
        best_path = path

# Format output
output_path = ' -> '.join([start_point] + list(best_path) + [start_point])
output_cost = f"Cost: {shortest_distance:.2f}"

print(output_path)
print(output_cost)

# Python code to visualize the tour, and mark each movement with an arrow.
import matplotlib.pyplot as plt

# Extract coordinates
x = [points[start_point][0]] + [points[p][0] for p in best_path] + [points[start_point][0]]
y = [points[start_point][1]] + [points[p][1] for p in best_path] + [points[start_point][1]]

# Plotting
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'o-', mfc='r')  # Points and lines
for i in range(len(x) - 1):
    plt.arrow(x[i], y[i], x[i + 1] - x[i], y[i + 1] - y[i], head_width=0.2, length_includes_head=True)
    
# Marking places
for name, coord in points.items():
    plt.text(coord[0], coord[1], name)

plt.grid(True)
plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Shortest Path Visualization')
plt.show()