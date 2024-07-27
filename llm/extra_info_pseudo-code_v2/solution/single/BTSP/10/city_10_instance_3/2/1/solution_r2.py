import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)

def calculate_total_and_max_distance(tour, cities):
    total_distance = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
        total_distance += dist
        max_distance = max(max_distance, dist)
    # Return to the depot from the last city in the tour
    dist = euclidean_distance(cities[tour[-1]], cities[tour[0]])
    total_distance += dist
    max_distance = max(max_distance, dist)
    return total_distance, max_distance

def solve_BTSP(cities):
    num_cities = len(cities)
    city_indices = list(range(num_cities))
    
    best_tour = None
    best_max_distance = float('inf')
    best_total_distance = float('inf')
    
    for perm in permutations(city_indices[1:]):  # Generate permutations of cities excluding the depot
        tour = [0] + list(perm) + [0]  # Start and end at depot city
        total_distance, max_distance = calculate_total_and_max_distance(tour, cities)
        
        if max_distance < best_max_distance or (max_distance == best_max_distance and total_distance < best_total_distance):
            best_tour = tour
            best_total_distance = total_distance
            best_max_distance = max_distance
    
    return best_tour, best_total_distance, best_max_distance

# Define the coordinates for each city
cities = [
    (84, 67),  # City 0 - Depot
    (74, 40),  # City 1
    (71, 13),  # City 2
    (74, 82),  # City 3
    (97, 28),  # City 4
    (0, 31),   # City 5
    (8, 62),   # City 6
    (74, 56),  # City 7
    (85, 71),  # City 8
    (6, 76)    # City 9
]

best_tour, best_total_distance, best_max_distance = solve_BTSP(cities)

print("Tour:", best_tour)
print("Total travel cost:", round(best_total_distance, 2))
print("Maximum distance between consecutive cities:", round(best_max_distance, 2))