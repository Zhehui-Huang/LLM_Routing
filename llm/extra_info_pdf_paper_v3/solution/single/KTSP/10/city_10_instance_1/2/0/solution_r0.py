import math
from itertools import permutations

# City coordinates with city index as key
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Compute Euclidean distance
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Create distance matrix
distance_matrix = {}
for i in cities:
    distance_matrix[i] = {}
    for j in cities:
        distance_matrix[i][j] = distance(i, j)

# Helper function to calculate total tour cost
def calculate_tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i+1]]
    return cost

# Variable to store the best tour and its cost
best_tour = None
best_cost = float('inf')

# Iterate over all combinations of 4 other cities plus the depot
from itertools import combinations

all_combinations = combinations([i for i in range(1, 10)], 4)  # Exclude depot initially, and pick 4 as we include depot later

# Compute costs for all permutations of cities in each combination
for comb in all_combinations:
    current_cities = [0] + list(comb)  # Always start at the depot
    permutations_of_cities = permutations(current_cities)
    for perm in permutations_of_cities:
        # Always return to the depot
        current_tour = list(perm) + [0]
        current_cost = calculate_tour_cost(current_tour)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour

# Output the result as per the required format
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")