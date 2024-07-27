import itertools
import math

# Define the cities with their coordinates
cities = {
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

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Get all combinations of 5 non-depot cities (since the depot is mandatory)
combinations = itertools.combinations([i for i in range(1, 15)], 5)

best_tour = None
best_cost = float('inf')

# Test all combinations of cities
for combo in combinations:
    # Include the depot city (0) in each tour
    full_tour = [0] + list(combo) + [0]
    
    # Get all permutations of the internal cities to find the minimal route
    for perm in itertools.permutations(combo):
        current_tour = [0] + list(perm) + [0]
        current_cost = sum(euclidean_distance(current_tour[i], current_tour[i+1]) for i in range(len(current_tour)-1))
        
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour

# Print the best tour found and its cost
print(f"Tour: {best_tour}")
print(f"Total travel cost: {best_cost:.2f}")