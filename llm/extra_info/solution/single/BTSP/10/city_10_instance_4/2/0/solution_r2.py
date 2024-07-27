import math
from itertools import permutations

# Cities' coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Compute Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Calculate all pairs distances
distances = {}
for city1 in cities:
    for city2 in cities:
        if city1 != city2:
            distances[(city1, city where)] = calculate_distance(city1, city2)

# Find a tour minimizing the longest distance between consecutive cities using permutations (infeasible for larger sets)
def find_optimal_tour():
    min_max_distance = float('inf')
    best_tour = None
    all_cities = list(cities.keys())[1:]  # Exclude the depot from permutation list
    for perm in permutations(all_cities):
        tour = [0] + list(perm) + [0]
        max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
    # Calculate the total distance of the tour
    total_distance = sum(distances[(best_tour[i], best_tour[i+1])] for i in range(len(best_tour) - 1))
    return best_tour, total_distance, min_max_distance

# Call function and print results
tour, total_cost, max_consecutive_distance = find_optimal_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_consecutive_distance}")