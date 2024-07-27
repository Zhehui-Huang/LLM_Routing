import numpy as np
import random

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def initialize_pheromone_matrix(size, initial_pheromone):
    return np.full((size, size), initial_pheromone)

def calculate_choice_info(pheromone_matrix, distance_matrix, alpha, beta):
    heuristic_info = 1 / (distance_matrix + 1e-10)  # to avoid division by zero
    return (pheromone_matrix ** alpha) * (heuristic_info ** beta)

def update_pheromone(pheromone_matrix, route, cost, rho):
    for j in range(len(route) - 1):
        start, end = route[j], route[j + 1]
        pheromone_matrix[start][end] += 1.0 / cost
    pheromone_matrix *= (1 - rho)
    return pheromone_matrix

def ant_tour(depot, num_cities, distance_matrix, pheromone_matrix, alpha, beta):
    route = [depot]
    allowed = list(range(num_cities))
    allowed.remove(depot)

    while allowed:
        current = route[-1]
        choice_info = calculate_choice_info(pheromone_matrix[current, :], distance_matrix[current, :], alpha, beta)
        probabilities = choice_info[allowed] / np.sum(choice_info[allowed])
        next_city = np.random.choice(allowed, p=probabilities)
        route.append(next_city)
        allowed.remove(next_city)

    route.append(depot)  # Return to depot
    cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    return route, cost

def ant_colony_optimization(coordinates, num_ants, num_cycles, alpha, beta, rho, initial_pheromone, depots):
    num_cities = len(coordinates)
    distance_matrix = np.array([[euclidean_distance(coordinates[i], coordinates[j]) 
                                for j in range(num_cities)] 
                                for i in range(num_cities)])
    results = []

    for depot in depots:
        pheromone_matrix = initialize_pheromone_matrix(num_cities, initial_pheromone)
        best_cost = float('inf')
        best_route = None
    
        for cycle in range(num_cycles):
            for ant in range(num_ants):
                route, cost = ant_tour(depot, num_cities, distance_matrix, pheromone_matrix, alpha, beta)
                if cost < best_cost:
                    best_cost = cost
                    best_route = route
                pheromone_matrix = update_pheromone(pheromone_matrix, route, cost, rho)
        
        results.append((best_route, best_cost))
    
    return results

# Parameters and execution
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)]

num_ants = 20
num_cycles = 100
alpha = 1.0
beta = 2.0
rho = 0.1
initial_pheromone = 0.1
depots = [0, 1]

tours = ant_colony_optimization(coordinates, num_ants, num_cycles, alpha, beta, rho, initial_pheromone, depots)

# Print results
for i, (tour, cost) in enumerate(tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    if i == 0:
        overall_cost = cost
    else:
        overall_cost += cost
        
print(f"Overall Total Travel Cost: {overall_cost}")