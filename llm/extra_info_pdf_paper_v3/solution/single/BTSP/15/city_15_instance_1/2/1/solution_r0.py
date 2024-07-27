import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tour, cities):
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return total_cost

def max_distance_in_tour(tour, cities):
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]], cities[tour[i]])
        if dist > max_distance:
            max_distance = dist
    return max_distance

# Define cities
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 5: (40, 57),
    6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 10: (4, 60), 11: (78, 82),
    12: (83, 96), 13: (60, 50), 14: (98, 1)
}

def find_optimal_tour(cities):
    city_indices = list(cities.keys())
    best_tour = None
    min_max_distance = float('inf')

    # Generate all possible tours using permutation, this is feasible since number of cities is small (15)
    for perm in permutations(city_indices[1:]):  # Permute only city 1 to 14, keeping 0 fixed as start and end
        current_tour = [0] + list(perm) + [0]
        current_max_distance = max_distance_in_tour(current_tour, cities)
        if current_max_distance < min_max_distance:
            min_max_distance = current_max_distance
            best_tour = current_tour

    total_cost = calculate_total_cost(best_tour, cities)
    return (best_tour, total_cost, min_max_distance)

# Calculate the optimal tour
optimal_tour, total_travel_cost, maximum_distance = find_optimal_tour(cities)

# Output results
print(f"Tour: {optimal_tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {maximum_distance}")