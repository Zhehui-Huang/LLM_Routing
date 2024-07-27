import numpy as np
import random

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def initialize_pheromone_matrix(size, initial_pheromone):
    return np.full((size, size), initial_pheromone)

def calculate_choice_info(pheromone_matrix, distance_matrix, alpha, beta):
    heuristic_info = 1 / (distance_matrix + 1e-10)  # to avoid division by zero
    return (pheromone_matrix ** alpha) * (heuristic_info ** beta)

def update_pheromone(pheromone_matrix, candidates, rho, quality):
    for i, route in enumerate(candidates):
        for j in range(len(route) - 1):
            start, end = route[j], route[j + 1]
            pheromone_matrix[start][end] += quality[i]
    pheromone_matrix *= (1 - rho)
    return pheromone_matrix

def ant_colony_optimization(coordinates, num_ants, num_cycles, alpha, beta, rho, initial_pheromone):
    num_cities = len(coordinates)
    pheromone_matrix = initialize_pheromone_matrix(num_cities, initial_pheromone)
    distance_matrix = np.array([[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)])
    
    best_routes = None
    best_cost = float('inf')
    
    for cycle in range(num_cycles):
        routes = []
        costs = []
        for ant in range(num_ants):
            depot = random.choice([0, 1])  # Robot 0 starts at depot 0, Robot 1 starts at depot 1
            
            route = [depot]
            allowed = list(range(num_cities))
            allowed.remove(depot)
            
            while allowed:
                current = route[-1]
                choice_info = calculate_choice_info(pheromone_matrix, distance_matrix[current, :], alpha, beta)
                probabilities = choice_info[allowed] / np.sum(choice_info[allowed])
                next_city = np.random.choice(allowed, p=probabilities)
                route.append(next_city)
                allowed.remove(next_city)
            
            route.append(depot)  # return to depot
            routes.append(route)
            costs.append(sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)))
        
        # Find best solution in this cycle
        min_cost = min(costs)
        if min_cost < best_cost:
            best_cost = min_cost
            best_routes = [routes[i] for i in range(num_ants) if costs[i] == min_cost]
        
        # Update pheromone
        quality = [1 / cost for cost in costs]
        pheromone_matrix = update_pheromone(pheromone_matrix, routes, rho, quality)
    
    return best_routes, best_cost

# City coordinates (index corresponds to city number)
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

# Ant Colony Optimization parameters
num_ants = 20
num_cycles = 100
alpha = 1.0
beta = 2.0
rho = 0.5
initial_pheromone = 0.1

# Run optimization
tours, total_cost = ant_colony_optimization(coordinates, num_ants, num_cycles, alpha, beta, rho, initial_pheromone)

# Output result
print(f'Robot 0 Tour: {tours[0]}')
print(f'Robot 0 Total Travel Cost: {total_cost[0]}')
print(f'Robot 1 Tour: {tours[1]}')
print(f'Robot 1 Total Travel Cost: {total_cost[1]}')
print(f'Overall Total Travel Cost: {sum(total_cost)}')