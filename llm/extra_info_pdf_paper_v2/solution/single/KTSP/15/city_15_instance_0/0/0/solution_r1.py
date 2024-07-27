import itertools
import math

# Define cities' coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return math.sqrt((cities[city_a][0] - cities[city_b][0])**2 + (cities[city_a][1] - cities[city_b][1])**2)

# Generate combinations of 3 cities excluding the depot
combinations = itertools.combinations([i for i in range(1, 15)], 3)

# Initialize variables to track the minimal tour cost and its corresponding tour
min_cost = float('inf')
optimal_tour = []

# Evaluate each combination
for combo in combinations:
    current_combo = [0] + list(combo) + [0]
    
    # Permute the inner cities to get all possible tours
    for perm in itertools.permutations(current_combo[1:-1]):
        # Complete the tour by adding the depot back
        tour = [0] + list(perm) + [0]
        
        # Calculate the cost of the current tour
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update minimum cost and optimal tour if current is better
        if cost < min_cost:
            min_cost = cost
            optimal_tour = tour

# Output the optimal tour and its cost
print("Tour:", optimal_tour)
print("Total travel cost:", round(min_cost, 2))