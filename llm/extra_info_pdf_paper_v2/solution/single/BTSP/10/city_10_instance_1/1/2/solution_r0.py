import math
from scipy.sparse.csgraph import minimum_spanning_tree
from scipy.sparse import csr_matrix
import numpy as np

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def get_distances(cities):
    num_cities = len(cities)
    distances = [[0] * num_cities for _ in range(num_cities)]
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = calculate_distance(cities[i], cities[j])
    return distances

def find_mst(distances):
    mst_matrix = minimum_spanning_tree(csr_matrix(distances))
    return mst_matrix.toarray().astype(float)

def find_tour(mst, start_city):
    num_cities = len(mst)
    visited = set()
    tour = []
    
    def dfs(city):
        visited.add(city)
        tour.append(city)
        for next_city in range(num_cities):
            if mst[city, next_city] > 0 and next_city not in visited:
                dfs(next_city)
    
    dfs(start_city)
    tour.append(start_city)  # return to the depot
    return tour

def compute_tour_details(tour, distances):
    total_cost = 0
    max_distance = 0
    
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        dist = distances[city_from][city_to]
        total_cost += dist
        max_distance = max(max_distance, dist)
    return total_cost, max_distance

def solve_btsp(cities):
    distances = get_distances(cities)
    mst = find_mst(distances)
    tour = find_tour(mst, 0)
    total_cost, max_distance = compute_tour_details(tour, distances)
    return tour, total_cost, max_distance

# Define city coordinates
cities = [(53, 68), (75, 11), (91, 95), (22, 80), (18, 63), (54, 91), (70, 14), (97, 44), (17, 69), (95, 89)]

# Calculate the optimal BTSP tour
tour, total_cost, max_distance = solve_btsp(cities)

# Output the result
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)