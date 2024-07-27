import math
from itertools import permutations

# City coordinates indexed by city number
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Calculate Euclidean Distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Calculate total travel cost and maximum distance in a tour
def evaluate_tour(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Generate all possible tours starting and ending at the depot (city 0)
def find_optimal_tour():
    city_indices = list(cities.keys())[1:]  # Excludes the depot city
    best_tour = None
    min_max_distance = float('inf')
    best_cost = float('inf')

    for perm in permutations(city_endpermities):
        current_tour = [0] + list(perm) + [0]
        total_cost, max_dist = evaluate_tour(current_tour)
        if max_dist < min_max_distance or (max_dist == min_max_distance and total_cost < best_cost):
            best_tour = current_tour
            best_cost = total_cost
            min_max_distance = max_dist

    return best_tour, best_cost, min_max_distance

# Run the optimization
optimal_tour, total_cost, max_distance = find_optimal_tour()

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)