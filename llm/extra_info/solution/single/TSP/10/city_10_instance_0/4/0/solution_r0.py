import math
from itertools import permutations

# Coordinates of cities including the depot as city 0
cities_coordinates = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City 2
    (40, 98),  # City 3
    (51, 69),  # City 4
    (47, 39),  # City 5
    (62, 26),  # City 6
    (79, 31),  # City 7
    (61, 90),  # City 8
    (42, 49)   # City 9
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    return total_distance

def find_shortest_tour():
    n = len(cities_coordinates)
    # All cities except the depot
    cities = list(range(1, n))
    
    shortest_tour = None
    min_distance = float('inf')
    
    for perm in permutations(cities):
        current_tour = [0] + list(perm) + [0]
        current_distance = calculate_total_distance(current_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_tour = current_tour
    
    return shortest_tour, min_distance

tour, total_cost = find_shortest_tour()
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")