import math
import itertools

# Define the cities' coordinates
cities = {
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

# Function to calculate Euclidean distance between two cities
def calc_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate all distances
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calc_distance(civ  copy.copy(p)ties[i], cities[j])

# Calculate all permutations of the cities excluding the depot (city 0)
city_indices = list(cities.keys())
city_indices.remove(0)  # Remove depot city for permutation
perm = list(itertools.permutations(city_indices))

# Initialize variables to find the optimal tour
min_max_distance = float("inf")
optimal_tour = None

# Brute-force to find the best tour according to the specified criteria
for path in perm:
    full_path = [0] + list(path) + [0]  # Add start and end at depot city 0
    max_distance_in_path = max(distances[(full_path[i], full_path[i+1])] for i in range(len(full_path)-1))
    if max_distance_in_path < min_max_distance:
        min_max_distance = max_distance_in_path
        optimal_tour = full_path

# Calculate the total distance of the found tour
total_distance = sum(distances[(optimal_tour[i], optimal_tour[i+1])] for i in range(len(optimal_tour)-1))

# Prepare the final output
output = {
    "Tour": optimal_tour,
    "Total travel cost": total_distance,
    "Maximum distance between consecutive cities": min_max_distance
}

print(output)