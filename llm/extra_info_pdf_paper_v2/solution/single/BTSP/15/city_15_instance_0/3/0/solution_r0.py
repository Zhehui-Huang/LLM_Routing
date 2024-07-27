import math
from itertools import permutations

# Coordinates of cities including the depot city at index 0
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create a complete distance matrix
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def find_minimax_tour():
    # Start at depot city 0, explore all permutations of other cities
    best_max_distance = float('inf')
    best_tour = None
    all_cities = list(range(1, len(cities)))  # All city indices except depot
    for perm in permutations(all_cities):
        tour = [0] + list(perm) + [0]
        max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
        if max_distance < best_max_distance:
            best_max_distance = max_distance
            best_tour = tour
    total_cost = sum(distances[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
    return best_tour, total_cost, best_max_distance

# Finding the tour, total cost, and maximum distance between consecutive cities
tour, total_cost, max_distance = find_minimax_tour()

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")