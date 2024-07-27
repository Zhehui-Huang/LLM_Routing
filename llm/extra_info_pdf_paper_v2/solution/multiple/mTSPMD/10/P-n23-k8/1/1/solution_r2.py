import numpy as np
import random
import math

# Define coordinates of each city including depots
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Compute Euclidean distance between pairs of cities
def calculate_distance_matrix(coords):
    n = len(coords)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = np.hypot(coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])
    return matrix

distance_matrix = calculate_distance_matrix(coordinates)

# Initialize parameters
num_robots = 8
num_ants = 40
num_iterations = 100
alpha = 1.0
beta = 5.0
rho = 0.5
pheromone_initial = 1 / np.mean(distance_Distance_matrix) / len(coordinates)

pheromones = np.full((len(coordinates), len(coordinates)), pheromone_initial)

# Helper functions for managing pheromone updates and solution construction
def update_pheromone_routes(routes, costs):
    for k in range(len(routes)):
        route = routes[k]
        cost = costs[k]
        for i in range(len(route) - 1):
            pheromones[route[i]][route[i+1]] += 1 / cost
            pheromones[route[i+1]][route[i]] += 1 / cost  # Symmetrical update

def construct_solution():
    all_tours = []
    all_costs = []
    for robot in range(num_robots):
        tour = [robot]
        current_city = robot
        unvisited = set(range(num_robots, len(coordinates)))  # Only non-depot cities at the beginning
        while unvisited:
            probabilities = []
            for city in unvisited:
                trail = pheromones[current_city][city] ** alpha * ((1 / distance_matrix[current_city][city]) ** beta)
                probabilities.append(trail)
            probabilities /= np.sum(probabilities)
            next_city = np.random.choice(list(unvisited), p=probabilities)
            tour.append(next_city)
            current_city = next_city
            unvisited.remove(next_city)
        tour.append(robot)  # Return to depot
        all_tours.append(tour)
        all_costs.append(sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1)))
    return all_tours, all_costs

# Main loop for ant colony optimization
global_best_cost = float('inf')
global_best_tours = None
for iteration in range(num_iterations):
    routes, costs = construct_solution()
    if sum(costs) < global_best_cost:
        global_best_cost = sum(costs)
        global_best_tours = routes
    for i in range(len(pheromones)):
        pheromones[i] *= (1 - rho)  # Evaporation
    update_pheromone_routes(routes, costs)

# Output the results
print(f"Overall Total Travel Cost: {global_best_cost}")
for r, route in enumerate(global_best_tours):
    route_cost = sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    print(f"Robot {r} Tour: {route}")
    print(f"Robot {r} Total Travel Cost: {route_cost}")