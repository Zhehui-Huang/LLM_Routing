import math
from itertools import permutations
from sys import maxsize


def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def find_bottleneck_tour(cities):
    n = len(cities)
    
    # Calculate all pairwise distances
    distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

    # Try exhaustive permutation method (feasible since n is relatively small)
    min_bottleneck_value = maxsize
    optimal_tour = None
    
    # Generate all possible tours using permutations (ignoring the depot return requirement)
    for perm in permutations(range(1, n)):
        current_tour = [0] + list(perm) + [0]
        max_edge_cost = max(distances[current_tour[i]][current_tour[i+1]] for i in range(len(current_tour) - 1))
        
        if max_edge_cost < min_bottleneck_value:
            min_bottleneck_value = max_edge_cost
            optimal_tour = current_tour

    # Calculate the total travel cost of the best tour
    total_travel_cost = sum(distances[optimal_tour[i]][optimal_tour[i+1]] for i in range(len(optimal_tour) - 1))

    return {
        "tour": optimal_tour,
        "total_travel_cost": total_travel_cost,
        "maximum_distance_between_consecutive_cities": min_bottleneck_value
    }


# Defining city coordinates
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95), 
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16), (4, 43), 
    (53, 76), (19, 72)
]

# Find the BTSP tour
results = find_bottleneck_tour(cities)

# Output the results
print(f"Tour: {results['tour']}")
print(f"Total travel cost: {results['total_travel_cost']:.2f}")
print(f"Maximum distance between consecutive cities: {results['maximum_distance_between_consecutive_cities']:.2f}")