import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def calculate_tour(tour, coordinates):
    total_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

def solve_tsp_bottleneck(coordinates):
    min_max_distance = float('inf')
    best_tour = None
    all_cities = list(range(1, len(coordinates)))  # exclude the depot city
    
    # Truncate the number of cities for demonstrative purposes
    all_cities = all_cities[:5]  # Only including the first 5 cities (plus depot)

    # Generate all permutations of a subset of cities
    for perm in permutations(all_cities):
        current_tour = [0] + list(perm) + [0]
        total_cost, max_distance = calculate_tour(current_tour, coordinates)
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = current_tour

    total_cost, max_distance = calculate_tour(best_tour, coordinates)
    return best_tour, total_cost, max_distance

# Define coordinates of the cities including depot for a small subset
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22)
]

# Solve the TSP with bottleneck optimization for a smaller set
tour, total_cost, max_distance = solve_tsp_bottleneck(coordinates)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)