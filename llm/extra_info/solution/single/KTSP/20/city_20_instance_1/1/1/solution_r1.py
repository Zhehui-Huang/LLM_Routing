import itertools
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_distance(path, coordinates):
    total_distance = 0
    for k in range(len(path) - 1):
        total_distance += euclidean_distance(coordinates[path[k]], coordinates[path[k+1]])
    return total_distance

# Coordinates of the cities, including the depot as the first city
coordinates = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98),
    (45, 84), (4, 56), (54, 82), (37, 28), (27, 45),
    (90, 85), (98, 76), (6, 19), (26, 29), (21, 79),
    (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

# Generate all combinations of 6 cities excluding the depot, then add the depot to each combination
combinations = itertools.combinations(range(1, 20), 6)
min_distance = float('inf')
best_path = None

for comb in combinations:
    # Add the depot city to each combination and consider all permutations
    current_combination = [0] + list(comb) + [0]
    for perm in itertools.permutations(current_combination):
        if perm[0] == 0 and perm[-1] == 0:  # Ensure it starts and ends at the depot
            current_distance = calculate_total_distance(perm, coordinates)
            if current_distance < min_distance:
                min_distance = current_distance
                best_path = perm

# Output the results
print("Tour:", list(best_path))
print("Total travel cost:", min_distance)