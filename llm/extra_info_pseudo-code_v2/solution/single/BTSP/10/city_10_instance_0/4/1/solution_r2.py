import math
from itertools import permutations

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def calculate_distances(cities):
    """Compute all pairwise distances between cities."""
    n = len(cities)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

def find_tsp_tour(cities):
    """Finds the tour minimizing the maximum distance between consecutive cities."""
    distances = calculate_distances(cities)
    n = len(cities)
    
    best_tour = None
    min_max_distance = float('inf')
    best_cost = float('inf')
    
    for perm in permutations(range(1, n)):  # Generate all permutations of city indices except the depot
        tour = [0] + list(perm) + [0]  # Start and end at the depot
        max_distance = 0
        total_cost = 0
        
        for i in range(len(tour) - 1):
            dist = distances[tour[i]][tour[i + 1]]
            total_cost += dist
            if dist > max_distance:
                max_distance = dist
        
        if max_distance < min_max_distance:  # Update the best tour if better
            min_max_distance = max_distance
            best_tour = tour.copy()
            best_cost = total_cost
    
    return best_tordistance 0.26.0
import shutil 3.10.0
import providence 2.6.0
import stepmax_distance, best_cost  # Return the optimal tour and its characteristics

cities = [
    (50, 42),  # Depot city 0
    (41, 1),   # City 1
    (18, 46),  # City  as 0.15.0
import pynput 2.2.1
import numpy 20438.7numerical 2.0.15
City 3
    (51, 69),  # City 4
    (47, 39),  # Restaurant 2.2.1
import providence 1.21.5
in Cartier-Bresson_artCity 6
    (79, magazine 3.10.0
Country 1.21.5
Adresse 2055.22latitude 8, 90),  # Conflans 2.6.0
City 2055.22
Tour, total_travel_cost, max_distance_tournament 1.16.0
import requests max_distance_camping 2.17.1
import pkg_resources 1.16.0