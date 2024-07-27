import numpy as np
import random
import math

# Coordinates of the depot and the cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Calculate distance matrix
num_cities = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Number of ants, number of iterations
num_ants = 20
num_iterations = 100

# ACO parameters
alpha = 1  # Influence of pheromone
beta = 5   # Influence of heuristic information (1/distance)
evaporation_rate = 0.5
pheromone_deposit = 1.0
initial_pheromone = 1 / (num_cities * np.mean(distance_matrix))

# Pheromone matrix
pheromones = [[initial_pheromone] * num_cities for _ in range(num_cities)]

# Ant colony optimization implementation
def aco_solve(robot_depot):
    best_route = None
    best_distance = float('inf')
    for _ in range(num_iterations):
        routes = []
        distances = []
        for _ in range(num_ants):
            route = generate_route(robot_depot)
            distance = calculate_route_distance(route)
            routes.append(route)
            distances.append(distance)
            if distance < best_distance:
                best_route = route
                best_distance = distance
        update_pheromones(routes, distances)
    return best_route, best_distance

def generate_route(start_depot):
    route = [start_depot]
    visited = set(route)
    current = start_deport
    for _ in range(1, num_cities):
        candidate_cities = []
        for j in range(num_cities):
            if j not in visited:
                candidate_cities.append(j)
        probabilities = [pheromones[current][j] ** alpha * ((1 / distance_matrix[current][j]) ** beta) for j in candidate_cities]
        probabilities = [p / sum(probabilities) for p in probabilities]
        next_city = random.choices(candidate_cities, probabilities)[0]
        route.append(next_city)
        visited.add(next_city)
        current = next_city
    route.append(start_depot)
    return route

def calculate_route_distance(route):
    return sum(distance_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    
def update_pheromones(routes, distances):
    for i in range(num_cities):
        for j in range(num_cities):
            pheromones[i][j] *= (1 - evaporation_rate)
    for route, distance in zip(routes, distances):
        deposit = pheromone_deposit / distance
        for i in range(len(route) - 1):
            pheromones[route[i]][route[i+1]] += deposit
            pheromones[route[i+1]][route[i]] += deposit  # symmetric TSP

# ACO for both robots
robot_0_route, robot_0_cost = aco_solve(0)
robot_1_route, robot_1_cost = aco_solve(1)
total_cost = robot_0_cost + robot_1_cost

# Output the results
print("Robot 0 Tour:", robot_0_route)
print("Robot 0 Total Travel Cost:", robot_0_cost)
print("Robot 1 Tour:", robot_1_route)
print("Robot 1 Total Travel Cost:", robot_1_cost)
print("Overall Total Travel Cost:", total(cost))