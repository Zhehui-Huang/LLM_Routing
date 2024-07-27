import itertools
import math

# City coordinates
coordinates = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# City groups
groups = {
    0: [1, 2, 6],
    1: [3, 7, 8],
    2: [4, 5, 9]
}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Generate all combinations of cities, one from each group
all_combinations = itertools.product(groups[0], groups[1], groups[2])

# Depot city
depot = 0

# Check every combination to find the shortest path
shortest_distance = float('inf')
shortest_tour = None

for combination in all_combinations:
    # Permutations of the combination to find the shortest path for the given combination
    for perm in itertools.permutations(combination):
        # Calculate the path distance: depot -> city from group 0 -> city from group 1 -> city from group 2 -> depot
        path_distance = euclidean_distance(depot, perm[0]) + \
                        euclidean_distance(perm[0], perm[1]) + \
                        euclidean_distance(perm[1], perm[2]) + \
                        euclidean_distance(perm[2], depot)
        if path_distance < shortest_distance:
            shortest_distance = path_distance
            shortest_tour = [depot] + list(perm) + [depot]

# Output the shortest tour and its distance
output = f"Tour: {shortest_tour}\nTotal travel cost: {shortest_distance:.2f}"
print(output)