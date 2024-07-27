import math
import itertools

def euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_distance(tour, coordinates):
    """Calculate the total distance for a given tour."""
    distance = 0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i - 1]]
        x2, y2 = coordinates[tour[i]]
        distance += euclidean_distance(x1, y1, x2, y2)
    # Add distance back to the depot
    x1, y1 = coordinates[tour[-1]]
    x2, y2 = coordinates[tour[0]]
    distance += euclidean_distance(x1, y1, x2, y2)
    return distance

# Provided coordinates of cities including the depot
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Number of cities to visit including the depot
cities_to_visit = 6
city_indices = list(coordinates.keys())
all_combinations = list(itertools.combinations(city_indices, cities_to_visit))
filtered_combinations = [comb for comb in all_combinations if 0 in comb]  # Ensure that depot city is included

# Find the shortest valid tour
shortest_distance = float('inf')
best_tour = None

for combination in filtered_combinations:
    for perm in itertools.permutations(combination):
        if perm[0] == 0 and perm[-1] == 0:  # Ensure tours start and end at the depot
            tour_distance = total_distance(perm, coordinates)
            if tour_distance < shortest_distance:
                shortest_distance = tour_distance
                best_tour = perm

# Display the results
print("Tour:", list(best_tour))
print("Total travel cost:", round(shortest_distance, 2))