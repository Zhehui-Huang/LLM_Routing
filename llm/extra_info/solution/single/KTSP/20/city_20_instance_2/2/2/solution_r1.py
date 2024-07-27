import itertools
import math

# Define the coordinates of the cities
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Generate all combinations of 9 cities to combine with the depot
city_indices = list(cities.keys())[1:]
combinations = itertools.combinations(city_indices, 9)

# Initialize variables to store the minimum tour and cost
min_tour = None
min_cost = float('inf')

# Process each combination
for combination in combinations:
    all_cities = [0] + list(combination) + [0]  # Starting and ending at the depot
    perms = itertools.permutations(all_cities[1:-1])  # Generate permutations of the middle cities

    for perm in perms:
        tour = [0] + list(perm) + [0]
        # Calculate the total cost of this tour
        cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        
        # Update minimum cost and tour
        if cost < min_cost:
            min_cost = cost
            min_tour = tour

# Output the optimal tour and its total cost
print(f"Tour: {min_tour}")
print(f"Total travel cost: {min_cost}")