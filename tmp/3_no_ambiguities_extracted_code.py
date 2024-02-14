from itertools import permutations
import math
import matplotlib.pyplot as plt

# Places coordinates
places = {'Place 1': (9, 4), 'Place 2': (4, 6), 'Place 3': (4, 4), 'Place 4': (3, 4), 'Place 5': (4, 8)}

# Calculate distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Calculate total distance of a path
def total_distance(path):
    return sum(distance(places[path[i]], places[path[i + 1]]) for i in range(len(path) - 1))

# Generating all permutations of the places excluding the start place
perms = permutations([place for place in places if place != 'Place 1'])

# Adding start and end point to each permutation and calculating the total distance
min_distance = float('inf')
best_path = None
for perm in perms:
    path = ('Place 1',) + perm + ('Place 1',)
    current_distance = total_distance(path)
    if current_distance < min_distance:
        min_distance = current_distance
        best_path = path

# Output solution
print(' -> '.join(best_path))
print(f'Cost: {min_distance}')

# Visualization of the tour
def visualize_tour(path):
    fig, ax = plt.subplots()
    x = [places[place][0] for place in path]
    y = [places[place][1] for place in path]
    plt.plot(x, y, 'o-', markerfacecolor='red', markersize=10)

    for i, place in enumerate(path):
        plt.text(places[place][0], places[place][1], f'{place}', fontsize=12)
    
    # Adding arrows to indicate movement
    for i in range(len(path)-1):
        plt.arrow(x[i], y[i], x[i+1]-x[i], y[i+1]-y[i], head_width=0.15, head_length=0.15, fc='k', ec='k')
    
    ax.set_aspect('equal')
    plt.title('Tour Visualization')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.show()

visualize_tour(best_path)