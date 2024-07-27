import itertools
from math import sqrt

# Define the cities with their coordinates
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def distance(city1, city2):
    """ Calculate the Euclidean distance between two cities. """
    return sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# Prepare for finding the minimum cost tour
min_cost = float('inf')
optimal_tour = None

# Check each combination of 11 cities plus the depot city
for combo in itertools.combinations(range(1, 15), 11):
    # Include the depot city
    tour_cities = [0] + list(combo)
    # Find the minimal tour for this specific combination
    for perm in itertools.permutations(tour_cities):
        # Ensure the tour starts and ends at the depot
        tour = list(perm) + [0]
        # Calculate the tour cost
        cost = sum(distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
        # Update the minimal tour if found a new optimal one
        if cost < min_cost:
            min_cost = cost
            optimal_tour = tour

# Output the best tour and the traveled cost
print("Tour:", optimal_tours, "\nTotal travel cost:", round(min_cost, 2))