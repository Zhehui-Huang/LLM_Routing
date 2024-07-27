import math
import itertools
from collections import defaultdict

# City coordinates
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

# Calculate Euclidean distance between two points
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate all pairwise distances
def calculate_distances(cities):
    distances = {}
    for i in cities:
        for j in cities:
            if i != j:
                distances[(i, j)] = euclidean_distance(cities[i], cities[j])
    return distances

# TSP Solver
def solve_tsp_bruteforce(cities):
    city_indices = list(cities.keys())
    distances = calculate_distances(cities)

    min_tour = None
    min_cost = float('inf')
    max_distance_between_cities = float('inf')

    for tour in itertools.permutations(city_indices[1:]):
        tour = [0] + list(tour) + [0]  # Append depot city as start and end
        cost_of_tour = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
        max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
        
        if max_distance < max_distance_between_cities:
            min_tour = tour
            min_cost = cost_of_tour
            max_distance_between_cities = max_distance
    
    return min_tour, min_cost, max_distance_between_cities

# Solving TSP for given cities
tour, total_cost, max_distance = solve_tsp_bruteforce(cities)

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)