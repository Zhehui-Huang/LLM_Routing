import math
import itertools

# Coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Function to calculate the Euclidean distance between two cities
def distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Precompute distances between all pairs of cities
dist_matrix = {}
for i in cities:
    for j in cities:
        dist_matrix[(i, j)] = distance(i, j)

# Generate all combinations of 9 cities (excluding the depot)
city_combinations = itertools.combinations(range(1, 15), 9)

# Initialize variables to track the optimal tour
min_cost = float('inf')
best_tour = []

# Check each combination formed with the depot
for comb in city_combinations:
    possible_tour = [0] + list(comb) + [0]
    
    # Permutate the inner cities
    for permuted_path in itertools.permutations(comb):
        tour_path = [0] + list(permuted_path) + [0]
        tour_cost = sum(dist_matrix[(tour_path[i], tour_path[i + 1])] for i in range(len(tour_path) - 1))
        
        # Keep track of the minimum cost tour
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = tour_path

# Ensure the tour and cost are printed
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")