import itertools
import math

# Define city coordinates
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

# Function for calculating Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0]) ** 2 + (cities[a][1] - cities[b][1]) ** 2)

# Precompute distances between all pairs of cities
distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(i, j)

# Function to compute the total distance of a given tour
def calculate_route_cost(route):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distances[(route[i], route[i+1])]
    return total_cost

# Initialize the minimum cost variable
min_cost = float('inf')
best_route = []

# Generate all combinations of picking 9 cities (other than the depot) from the available 14 cities
for subset in itertools.combinations(range(1, 15), 9):
    potential_cities = list(subset)
    # Create all potential tours by permuting the selected cities and adding the depot as start and end
    for perm in itertools.permutations(potential_cities):
        tour = [0] + list(perm) + [0]
        cost = calculate_route_cost(tour)
        if cost < min_cost:
            min_cost = cost
            best_route = tour

# Output the best (shortest) tour found and its cost
print("Tour:", best_route)
print("Total travel cost:", min_cost)