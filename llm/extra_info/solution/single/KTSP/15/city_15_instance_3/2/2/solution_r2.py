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

# Precompute distances between all pairs of cities for quick lookup
dist_matrix = {(i, j): distance(i, j) for i in cities for j in cities}

# Generate all combinations of 9 cities (excluding the depot)
city_combinations = list(itertools.combinations(range(1, 15), 9)) # Only 9 cities must be selected

# Function to calculate the total tour distance
def calculate_tour_cost(tour):
    return sum(dist_matrix[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Searching for the best tour
min_cost = float('inf')
best_tour = []

for combination in city_combinations:
    # Each combination needs to be test with all permutations for optimal path
    for permutation in itertools.permutations(combination):
        current_tour = [0] + list(permutation) + [0]
        current_cost = calculate_tour_cost(current_tour)
        
        if current_cost < min_cost:
            min_cost = current_cost
            best_tour = current_tour

# Print the results
print(f"Tour: {best_tour}")
print(f"Total travel cost: {min_cost:.2f}")