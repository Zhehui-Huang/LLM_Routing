import itertools
import math

# Coordinates of the cities
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
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


# Generate all 7-city combinations including the depot city 0
combinations = itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 6)
combinations = [comb for comb in combinations if 0 in comb]

# Search for the shortest tour within these combinations
min_distance = float('inf')
best_tour = None

for cities_subset in combinations:
    # Generate permutations to find the shortest path that visits all cities in the subset
    permutations = itertools.permutations(cities_subset)
    for perm in permutations:
        # Ensure we start and end at the depot
        tour = list(perm) + [0]
        if tour[0] == 0:
            # Calculate the tour distance
            total_distance = 0
            for i in range(len(tour) - 1):
                total_distance += distance(tour[i], tour[i + 1])
            # Update the minimum distance if the current tour is shorter
            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = tour

# Output the best tour and its corresponding total travel distance
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_distance:.2f}")