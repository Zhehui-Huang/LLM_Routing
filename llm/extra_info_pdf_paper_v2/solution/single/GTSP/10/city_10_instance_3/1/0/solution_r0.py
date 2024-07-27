import math
from itertools import permutations

# Define the city coordinates
cities = {
    0: (84, 67),  # Depot city
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

# Define the city groups
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Generate all combinations of choosing one city from each group
def possible_combinations(groups):
    if not groups:
        return []
    elif len(groups) == 1:
        return [[city] for city in groups[0]]
    else:
        result = []
        first_group = groups[0]
        rest_combinations = possible_combinations(groups[1:])
        for city in first_group:
            for combination in rest_combinations:
                result.append([city] + combination)
        return result

# Find the optimal tour that minimizes the travel cost
def find_optimal_tour(groups):
    all_combinations = possible_combinations(groups)
    best_tour = None
    minimal_cost = float('inf')
    
    for comb in all_combinations:
        # Consider each permutation of the cities in the combination
        for perm in permutations(comb):
            # Build the tour from the depot to each city in the permutation and back to depot
            tour = [0] + list(perm) + [0]
            # Calculate the total cost of this tour
            cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
            # Check if this tour has a lower cost than the current best
            if cost < minimal_cost:
                minimal_cost = cost
                best_tour = tour
    
    return best_tour, minimal_cost

# Calculate and return the optimal tour
optimal_tour, tour_cost = find_optimal_tour(groups)
print("Tour:", optimal_tour)
print("Total travel cost:", tour_cost)