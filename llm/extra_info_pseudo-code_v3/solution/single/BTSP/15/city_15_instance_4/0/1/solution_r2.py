import math
from itertools import permutations

# City coordinates provided
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
    (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities. """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate all distances
distances = [[calculate_distance(cities[i], cities[j]) for j in range(len(cities))] for i in range(len(cities))]

def find_btsp_tour(cities, distances):
    n = len(cities)
    min_bottleneck = float('inf')
    best_tour = None

    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_distance_in_tour = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        if max_distance_in_tour < min_bottleneck:
            min_bottleneck = max_distance_in_tour
            best_tour = tour

    if best_tour:
        total_cost = sum(distances[best_tour[i]][best_tour[i + 1]] for i in range(len(best_tour) - 1))
        return best_tour, total_cost, min_bottleneck
    else:
        return None

# Get the best tour along with its total travel cost and bottleneck distance
result = find_btsp_tour(cities, distances)

if result:
    tour, total_cost, max_distance = result
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("No valid tour was found.")