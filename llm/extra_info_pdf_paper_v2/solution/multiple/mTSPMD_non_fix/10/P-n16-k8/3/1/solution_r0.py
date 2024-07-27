import math
import numpy as np
import random
from collections import defaultdict

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def initialize_distance_matrix(coordinates):
    num_cities = len(coordinates)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])
            else:
                distances[i][j] = float('inf')
    return distances

def tabu_search(num_robots, depots, city_coords, iterations=1000, tabu_size=50, num_neighbors=20):
    def generate_initial_solution():
        non_depots = [i for i in range(len(city_coords)) if i not in depots]
        random.shuffle(non_depots)
        chunks = np.array_split(non_depots, num_robots)
        routes = [[depots[0]] + list(chunk) for chunk in chunks]
        return routes
    
    def total_cost(routes):
        cost = 0
        for route in routes:
            route_cost = 0
            for i in range(len(route) - 1):
                route_cost += distances[route[i]][route[i+1]]
            cost += route_cost
        return cost

    def create_neighbors(route):
        neighbors = []
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                new_route = route[:]
                new_route[i], new_route[j] = new_route[j], new_route[i]
                neighbors.append(new_route)
        return neighbors
    
    distances = initialize_distance_matrix(city_coords)
    best_solution = generate_initial_solution()
    best_cost = total_cost(best_solution)
    tabu_list = defaultdict(int)

    for iteration in range(iterations):
        neighbors = []
        for route in best_solution:
            neighbors.extend(create_neighbors(route))
        
        best_neighbor = None
        best_neighbor_cost = float('inf')
        
        for neighbor in neighbors:
            neighbor_cost = total