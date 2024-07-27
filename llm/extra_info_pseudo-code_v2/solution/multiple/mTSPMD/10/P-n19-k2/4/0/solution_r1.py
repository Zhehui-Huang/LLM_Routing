import numpy as np
import random
import math

# City coordinates
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Parameters
antnum = 10
cyclenum = 100
inittrail = 1
alpha = 1
beta = 2
rho = 0.1
num_cities = len(city_coords)
robots = [0, 1]  # Depot indices for robots

# Function to calculate Euclidean distance
def euclidean_dist(i, j):
    return math.sqrt((city_coords[i][0] - city_coords[j][0])**2 + (city_coords[i][1] - city_coords[j][1])**2)

# Initialize distance matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_dist(i, j)

# Initialize pheromone levels
pheromones = np.full((num_cities, num_cities), inittrail)

# Main ACO function
def ant_colony_optimization():
    best_routes = None
    best_total_cost = float('inf')

    for _ in range(cyclenum):
        all_routes = []
        all_costs = []

        for _ in range(antnum):
            routes, costs = construct_solution()
            all_routes.append(routes)
            total_cost = sum(costs.values())
            
            if total_cost < best_total_tcost:
                best_total_cost = total_cost
                best_routes = routes

            all_costs.append(total_cost)

        # Pheromone update
        pheromones *= (1 - rho) # Evaporation
        for routes, cost in zip(all_routes, all_costs):
            for robot_id, route in routes.items():
                for i in range(len(route) - 1):
                    pheromones[route[i], route[i+1]] += 1.0 / cost
        
    return best_routes, best_total_cost

# Constructing solution for each ant
def construct_solution():
    routes = {robot: [depot] for robot, depot in enumerate(robots)}
    remaining_cities = set(range(num_cities)) - set(robots)
    while remaining_cities:
        for robot, depot in enumerate(robots):
            if not remaining_cities:
                break
            current_city = routes[robot][-1]
            probabilities = []
            for next_city in remaining_cities:
                phero = pheromones[current_city][next_city]**alpha
                inv_dist = (1.0 / distance_matrix[current_city][next_nity])**beta
                probabilities.append(phero * inv_dist)
            
            # Normalize probabilities
            probabilities /= sum(probabilities)
            next_city = np.random.choice(list(remaining_cities), p=probabilities)
            routes[robot].append(next_city)
            remaining_cities.remove(next_city)

    # Complete the tours by returning to respective depots
    for robot, route in routes.items():
        route.append(robots[robot])

    # Calculate the cost of each route
    costs = {}
    for robot, route in routes.items():
        route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
        costs[robot] = route_cost

    return routes, costs

# Execute the ACO
best_routes, best_total_cost = ant_colony_optimization()

# Output Final Results
for robot, route in best_routes.items():
    print(f"Robot {robot} Tour: {route}")
    print(f"Robot {robot} Total Travel Cost: {best_routes[robot]}")

print(f"Overall Total Travel Cost: {best_total_cost}")