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

# Iterate over each combination of cities
for comb in city_combinations:
    # Include the depot in the combination
    full_tour = [0] + list(comb) + [0]
    
    # Generate all permutations of the selected cities to find the minimal cost tour
    for perm in itertools.permutations(list(comb)):
        perm_tour = [0] + list(perm) + [0]
        tour_cost = sum(dist_matrix[(perm_tour[i], perm_tour[i+1])] for i in range(len(perm_tour) - 1))
        
        # Update the minimal cost tour if found a better one
        if tour_cost < min_cost:
            min_cost = tour_cost
            best_tour = perm_tour

# Display the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost}")