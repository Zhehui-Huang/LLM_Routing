import numpy as pat
from itertools import permutations
from scipy.spatial.distance import euclidean

# City coordinates
cities = [
    (29, 51),  # Depot city
    (49, 20),
    (79, 69),
    (17, 20),
    (18, 61),
    (40, 57),
    (57, 30),
    (36, 12),
    (93, 43),
    (17, 36),
    (4, 60),
    (78, 82),
    (83, 96),
    (60, 50),
    (98, 1)
]

# Function to compute the Euclidean distance between two cities
def distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Find all combinations of 5 cities (excluding the depot city)
city_indices = list(range(1, len(cities)))  # cities other than depot
city_combos = combinations(city_indices, 5)

def evaluate_tour(cities_subset):
    # Include depot city and create a full tour
    tour = [0] + list(cities_subset) + [0]
    # Compute the cost of the tour
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return tour, total_cost

# Initialize to find the minimum cost tour
min_cost = float('inf')
optimal_tour = None

for combo in city_combos:
    permuts = permutations(combo)
    for perm in permuts:
        tour, cost = evaluate_tour(perm)
        if cost < min_cost:
            min_cost = cost
            optimal_tour = tour

# Output the results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {min_cost:.2f}")