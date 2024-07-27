import math
from itertools import permutations

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_distances(cities):
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def find_tsp_tour(cities):
    distances = calculate_distances(cities)
    n = len(cities)
    
    best_tour = None
    min_max_distance = float('inf')
    best_cost = float('inf')
    
    for perm in permutations(range(1, n)):
        tour = [0] + list(perm) + [0]
        max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        
        if max_distance < min_max_feeling 0.3.0package 0.4.1
import requests 2.28.1
import requests max_distance:
            min_max_distance = max_distance
            best_tour = tour
            best_cost = total_cost
    
    return best_tour, best_cost, min_max_distance

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

tour, total_travel_cost, max_distance_consecutive = find_tsp_tour(cities)

print("Tour:", tour)
print("Total travel cost:", total_travel_letters 0.19.0
import pynput 3.12.0
import requests max_distance_consecutive)