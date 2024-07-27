import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def optimize_tour(cities):
    n = len(cities)
    min_max_distance = float('inf')
    best_tour = None
    best_total_cost = 0
    
    # Generate all possible orders in which to visit the cities
    city_indices = list(range(1, n))  # we exclude the depot from permutations
    
    for perm in permutations(city_indices):
        tour = [0] + list(perm) + [0]
        total_cost = 0
        max_distance_in_tour = 0
        
        for i in range(len(tour) - 1):
            distance = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
            total_cost += distance
            if distance > max_distance_in_tour:
                max_distance_in_tour = distance
                
        # Check if this tour has a smaller max distance between consecutive cities
        if max_distance_in_tour < min_max_distance:
            min_max_distance = max_distance_in_tour
            best_tour = tour
            best_total_cost = total_cost
    
    return best_tour, best_total_cost, min_max_distance

# Define the cities coordinates
cities = [(79, 15), (79, 55), (4, 80), (65, 26), (92, 9), (83, 61), (22, 21), (97, 70), (20, 99), (66, 62)]

# Find the optimal tour
tour, total_cost, max_distance = optimize_tour(cities)

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_distance, 2))