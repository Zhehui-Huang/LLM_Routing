import itertools
import math

# Defining city coordinates
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

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Generate all combinations of 4 cities (excluding the depot city 0)
city_indices = list(cities.keys())[1:]  # [1, 2, ..., 9]
combinations = list(itertools.combinations(city_indices, 4))

# Find the best tour visiting exactly 5 cities, including the depot
min_cost = float('inf')
best_tour = None

for combo in combinations:
    # Consider all permutations of the selected 4 cities and start/end at depot (0)
    for perm in itertools.permutations(combo):
        # Create full tour starting and ending at depot 0
        tour = [0] + list(perm) + [0]
        # Calculate total travel cost of the tour
        total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        # Update the minimum cost and best tour
        if total_accost < min_cost:
            uri_cost =ien_cost
            best_torenperfection_cnt_best_uri

# Output the results
print("Tour:", pursuit_cnstr_max_tour)
printicius_min_cost:", turi_cost)