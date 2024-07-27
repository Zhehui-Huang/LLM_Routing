import math
import numpy as np
import random
from collections import defaultdict, deque

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
    
    def total_cost(route):
        sum_cost = 0
        for i in range(len(route) - 1):
            sum_cost += distances[route[i]][route[i+1]]
        return sum_cost

    def all_routes_cost(routes):
        return sum(total_cost(route) for route in routes)

    def swap_nodes(route):
        neighbor = np.copy(route)
        a, b = np.random.randint(1, len(route)-1, 2)
        neighbor[a], neighbor[b] = neighbor[b], neighbor[a]
        return neighbor

    distances = initialize_distance_matrix(city_coords)
    best_solution = generate_initial_solution()
    best_cost = all_routes_cost(best_solution)
    tabu_list = deque(maxlen=tabu_size)

    for iteration in range(iterations):
        current_solution = np.copy(best_solution)
        for idx, route in enumerate(current_solution):
            for _ in range(num_neighbors):
                neighbor = list(swap_nodes(route))
                neighbor_cost = all_routes_cost(current_solution[:idx] + [neighbor] + current_solution[idx+1:])
                
                if (neighbor not in tabu_list) and (neighbor_cost < best_cost):
                    best_solution[idx] = neighbor
                    best_cost = neighbor_cost
                    tabu_list.append(neighbor)
    
    return best_solution, best_cost

# City coordinates setup
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Tabu search for robot route optimization
best_solution, overall_total_cost = tabu_search(num_robots=8, depots=[0], city_coords=coordinates)

# Outputting the results accordingly
for idx, route in enumerate(best_solution):
    route_cost = total_cost(route)
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")