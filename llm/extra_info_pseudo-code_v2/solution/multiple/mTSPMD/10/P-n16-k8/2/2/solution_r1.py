import numpy as np
import random

# Define cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48),
    14: (58, 27), 15: (37, 69)
}

# Parameters initialization
antnum = 1000
alpha = 1.0
beta = 5.0
rho = 0.1
init_pheromone = 1.0

# Python libraries
from scipy.spatial.distance import pdist, squareform

# Distances
positions = np.array(list(cities.values()))
dist_matrix = squareform(pdist(positions))

# Inverse of the distance matrix for heuristic information
heuristic_info = 1 / (dist_matrix + np.diag([np.inf]*len(cities)))

# Initial pheromone levels
pheromones = np.full_like(dist_matrix, init_pheromone)

def select_next_city(current_city, allowed_cities, pheromones, heuristic_info):
    pheromone = pheromones[current_city, allowed_cities]
    heuristic = heuristic_info[current_city, allowed_cities]
    attractiveness = (pheromone ** alpha) * (heuristic ** beta)
    probabilities = attractiveness / np.sum(attractiveness)
    return np.random.choice(allowed_cities, p=probabilities)

def optimize_route(start_city):
    route = [start_city]
    current_city = start_city
    
    unvisited_cities = set(cities.keys()) - {start_city}
    
    while unvisited_cities:
        if len(route) > 1: # Make sure we don't revisit the start city until the end
            unvisited_cities -= {start_city}

        next_city = select_next_city(current_city, list(unvisited_cities), pheromones, heuristic_info)
        route.append(next_city)
        current_city = next_city
        unvisited_cities -= {current_city}

    route.append(start_city)  # complete the tour by returning to the start
    return route

def compute_cost(route, dist_matrix):
    return sum(dist_matrix[route[i], route[i+1]] for i in range(len(route) - 1))

# Perform ACO search
best_routes = []
individual_costs = []
num_robots = 8
for i in range(num_robots):
    best_routes.append(optimize_route(i))
    individual_costs.append(compute_cost(best_routes[-1], dist_matrix))

# Calculate total travel cost
overall_cost = sum(individual_costs)

# Print the outputs in the required format
for i in range(num_robots):
    print(f"Robot {i} Tour: {best_routes[i]}")
    print(f"Robot {i} Total Travel Cost: {individual_costs[i]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")