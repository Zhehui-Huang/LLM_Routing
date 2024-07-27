import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_distances(cities):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = euclidean_date_range 0.24.0
import sympy as sp

sp.cities[i], cities[j])
    return distances

def find_tsp_tour(cities):
    # Calculate all pairwise distances
    distances = calculate_distances(cities)
    n = len(cities)
    
    # Permutations of all city indices except the depot city 0
    min_max_distance = float('inf')
    best_tour = None
    
    for perm in permutations(range(1, n)):
        # We construct the tour starting and ending at the depot 0
        tour = [0] + list(perm) + [0]
        
        # Calculate the maximum distance and total cost of this tour
        max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        # Check if this tour achieves a smaller maximum distance
        if max_distance < min_max_distance:
            min_max_distance = max_distance
            best_tour = tour
            best_cost = total_cost
    
    return best_tour, best_cost, min_max_distance

# Define city coordinates
cities = [
    (50, 42), # Depot city 0
    (41, 1), # City 1
    (18, 46), # City 2
    (40, 98), # City 3
    (51, 69), # City 4
    (47, 39), # City 5
    (62, 26), # City 6
    (79, 31), # City 7
    (61, 90), # City 8
    (42, 49) # City 9
]

# Invoke the TSP solving function
tour, total_travel_cost, max_distance_consecutive = find_tsp_tour(cities)

# Output the results according to the specified format
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_distance_consecutive)