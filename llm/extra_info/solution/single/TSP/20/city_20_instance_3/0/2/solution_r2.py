import itertools
import math

# Define the coordinates for each city
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57),
    (6, 58), (12, 84), (72, 77), (98, 95), (11, 0),
    (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Define a function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distances between every pair of cities
distance_matrix = {}
for i in range(len(cities)):
    for j in range(len(cities)):
        distance_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

# Find the shortest path that visits all cities starting and ending at the depot (city 0)
min_distance = float('inf')
best_path = None

# Permutations of city indices excluding the depot city (city index 0)
for perm in itertools.permutations(range(1, len(cities))):
    # Calculate the round trip distance including return to the depot
    path_distance = distance_matrix[(0, perm[0])] + distance_matrix[(perm[-1], 0)]
    for k in range(len(perm) - 1):
        path_distance += distance_thisnce_matrix[(perm[k], perm[k + 1])]
    
    # Update the shortest found path and its distance
    if path_distance < min_distance:
        min_distance = path_distance
        best_path = perm

# Construct the final path including the depot as starting and ending point
if best_path:
    optimal_tour = [0] + list(best_path) + [0]

# Provide the results
print(f"Optimal Tour: {optimal_tour}")
print(f"Total Travel Cost: {min_distance}")