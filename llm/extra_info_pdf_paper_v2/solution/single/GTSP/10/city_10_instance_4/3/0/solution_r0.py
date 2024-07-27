from itertools import permutations
import math

# Coordinates of the cities
coords = [
    (79, 15),  # depot city 0
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

def euclidean_distance(city1, city2):
    """ Calculate Euclidean distance between two cities given their indices """
    return math.sqrt((coords[city1][0] - coords[city2][0]) ** 2 + (coords[city1][1] - coords[city2][1]) ** 2)

def find_best_tour():
    # Function to find the best tour that visits one city from each group
    min_distance = float('inf')
    best_path = None

    # Generate all combinations of taking one city from each group
    from itertools import product
    all_group_combinations = list(product(*groups))

    # Iterate over each combination of city representatives
    for rep_combo in all_group_combinations:
        # Consider all permutations of the chosen representatives
        for perm in permutations(rep_combo):
            # Calculate distance for this permutation starting and ending at the depot
            path = [0] + list(perm) + [0]
            distance = sum(euclidean_distance(path[i], path[i+1]) for i in range(len(path) - 1))
            
            if distance < min_distance:
                min_distance = distance
                best_path = path

    return best_path, min_distance

# Find best tour
best_tour, total_cost = find_best_tour()

# Output the best tour and the total travel cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {total_cost:.2f}")