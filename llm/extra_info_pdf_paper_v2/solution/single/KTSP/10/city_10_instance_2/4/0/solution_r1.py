import math
import itertools

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def total_distance(tour, coordinates):
    distance = 0
    for i in range(1, len(tour)):
        x1, y1 = coordinates[tour[i - 1]]
        x2, y2 = coordinates[tour[i]]
        distance += euclidean_distance(x1, y1, x2, y2)
    # Return to depot
    x1, y1 = coordinates[tour[-1]]
    x2, y2 = coordinates[tour[0]]
    distance += euclidean_distance(x1, y1, x2, y2)
    return distance

coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# Generate all possible combinations of k visiting cities, including the depot
cities_to_visit = 6
city_indices = list(coordinates.keys())
all_combinations = list(itertools.combinations(city_indices, cities_to_visit))
filtered_combinations = [comb for comb in all_combinations if 0 in comb]  # Ensure that depot city is included

# For each combination, generate all permutations to explore all possible tours
shortest_distance = float('inf')
best_tour = None

for combination in filtered_combinations:
    for perm in itertools.permutations(combination):
        if perm[0] == 0:  # Ensure tours start at depot
            tour_distance = total_distance(perm + (0,), coordinates)
            if tour_distance < shortest_distance:
                shortest_distance = tour_distance
                best_tour = perm + (0,)

print("Tour:", list(best_tour))
print("Total travel cost:", round(shortest_drawedistance, 2))