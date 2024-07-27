import math
import numpy as np
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def total_distance(tour, cities):
    distance = 0
    for i in range(1, len(tour)):
        distance += euclidean_distance(cities[tour[i-1]], cities[tour[i]])
    return distance

def find_best_k_tour(cities, k):
    all_city_indices = list(range(len(cities)))
    best_tour = None
    best_cost = float('inf')
    
    for subset in permutations(all_city_indices[1:], k - 1):  # generate permutations of cities excluding depot
        current_tour = [0] + list(subset) + [0]  # start and end at the depot city
        current_cost = total_distance(current_tour, cities)
        if current_cost < best_cost:
            best_cost = current_cost
            best_tour = current_tour
    
    return best_tour, best_cost

# Define the cities coordinates
cities = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# We need to find a tour of 8 cities (including the starting and returning to the depot)
k = 8

# Find the best tour and its cost
best_tour, best_cost = find_best_k_tour(cities, k)

# Print results
print("Tour:", best_tour)
print("Total travel cost:", round(best_cost, 2))