import math
from itertools import permutations

# City coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

# Calculate distances matrix
num_cities = len(cities)
distances = [[0]*num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distances[i][j] = euclidean_distance(cities[i], cities[j])

### Step 2: Generate all possible tours and find the one with the minimum maximum leg distance that starts and ends at depot 0

# Generating all permutations of cities except for the depot
min_max_leg_distance = float('inf')
best_tour = None

for perm in permutations(range(1, num_cities)):  # permutations of cities except the depot
    tour = [0] + list(perm) + [0]
    max_leg_distance = max(distances[tour[i]][tour[i + 1]] for i in range(num_cities))
    if max_leg_distance < min_max_leg_distance:
        min_max_leg_distance = max_leg_distance
        best_tour = tour

### Step 3: Calculate the total travel cost of the best tour
        
total_cost = sum(distances[best_tour[i]][best_tour[i + 1]] for i in range(num_cities))

### Step 4: Output the result
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {min_max_leg_distance:.2f}")