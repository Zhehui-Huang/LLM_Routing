import itertools
import math

# Coordinates of cities
city_coordinates = {
    0: (29, 51),
    1: (49, 20),
    2: (79, 69),
    3: (17, 20),
    4: (18, 61),
    5: (40, 57),
    6: (57, 30),
    7: (36, 12),
    8: (93, 43),
    9: (17, 36),
    10: (4, 60),
    11: (78, 82),
    12: (83, 96),
    13: (60, 50),
    14: (98, 1)
}

# City groups
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

def euclidean_distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def compute_minimal_tour():
    min_distance = float('inf')
    best_tour = []

    # Generate all combinations, one city from each group
    for cities in itertools.product(*city_groups):
        # Generate all permutations of the selected cities
        for permutation in itertools.permutations(cities):
            # Calculate total distance for the permutation tour starting and ending at the depot
            tour = [0] + list(permutation) + [0]
            total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

            if total_distance < min_distance:
                min_distance = total_distance
                best_tour = tour

    return best_tour, min_distance

# Solve for the optimal tour
optimal_tour, optimal_cost = compute_minimal_tour()

# Output the result
print("Tour:", optimal_tour)
print("Total travel cost:", optimal_cost)