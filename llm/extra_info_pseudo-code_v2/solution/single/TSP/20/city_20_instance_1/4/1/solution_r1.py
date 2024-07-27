import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def total_path_distance(cities, tour):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += euclidean_distance(cities[tour[i - 1]], cities[tour[i]])
    total_distance += euclidean_distance(cities[tour[-1]], cities[tour[0]])
    return total_distance

def find_shortest_tour(cities):
    city_indices = list(cities.keys())
    min_tour = None
    min_distance = float('inf')
    for perm in permutations(city_indices[1:]):  # exclude the first city (depot city 0)
        current_tour = [0] + list(perm) + [0]
        current_distance = total_path_distance(cities, current_tour)
        if current_distance < min_distance:
            min_distance = current_distance
            min_tour = current_tour
    return min_tour, min_distance

# Solving the Travelling Salesman Problem for the given cities
tour, distance = find_shortest_tour(cities)

# Output the tour and total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {distance:.2f}")