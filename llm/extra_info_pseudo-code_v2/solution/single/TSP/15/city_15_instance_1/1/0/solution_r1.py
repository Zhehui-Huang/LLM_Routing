import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_path_distance(tour, cities):
    distance = 0
    for i in range(len(tour) - 1):
        distance += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return distance

def find_shortest_tour(cities):
    n = len(cities)
    shortest_tour = None
    min_distance = float('inf')
    
    # We will check all permutations, skipping the first city (depot)
    for perm in permutations(range(1, n)):
        current_tour = [0] + list(perm) + [0]
        current_distance = total_path_distance(current_tour, cities)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_tour = current_tour
            
    return shortest_tour, min_distance

# Define the cities based on the given environment information
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), 
          (40, 57), (57, 30), (36, 12), (93, 43), (17, 36), 
          (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)]

# Solve TSP problem
tour, total_cost = find_shortest_tour(cities)
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")