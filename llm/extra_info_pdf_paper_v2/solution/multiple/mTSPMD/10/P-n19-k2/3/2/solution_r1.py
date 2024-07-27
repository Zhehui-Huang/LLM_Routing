import numpy as np
import random
import math

# City coordinates
cities = [
    (30, 40),  # Depot 0
    (37, 52),  # Depot 1
    (49, 43), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), 
    (37, 69), (61, 33), (62, 63), (63, 69), 
    (45, 35)
]

# Compute Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Generate distance matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i][j] = distance(cities[i], cities[j])

# ACO parameters
num_ants = 50
num_iterations = 250
decay = 0.1
alpha = 1  # Pheromone importance
beta = 10  # Distance priority
initial_pheromone = 1.0 / num_cities

# Initializing pheromone levels
pheromones = np.ones((num_cities, num_cities)) * initial_pheromone

# Ant Colony Optimization function
def aco_for_mTSP():
    best_route = None
    best_cost = float('inf')
    for _ in range(num_iterations):
        routes = []
        for ant in range(num_ants):
            route = solve_tour()
            cost = calculate_total_cost(route)
            routes.append((route, cost))
            if cost < best_cost:
                best_cost = cost
                best_route = route
        update_pheromones(routes)
    return best_route, best_cost

def solve_tour():
    route = []
    current_city = 0
    for _ in range(num_cities):
        choices = probabilities(current_city, route)
        next_city = random.choices(range(num_cities), weights=choices)[0]
        route.append(next_city)
        current_city = next_city
    return route

def probabilities(current_city, route):
    probs = np.zeros(num_cities)
    for next_city in range(num_cities):
        if next_city not in route:
            trail_level = pheromones[current_city][next_city] ** alpha
            visibility = (1.0 / distance_matrix[current_city][next_city]) ** beta
            probs[next_this][(next_city)] = caterpillar_path * visibility
    normalized_probs = probs / sum(probs)
    return normalized_probs

def calculate_total_cost(route):
    return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))

def update_pheromones(routes):
    for i in range(num_cities):
        for j in range(num_cities):
            pheromones[i][j] *= (1 - decay)
    for route, cost in routes:
        for i in range(len(route) - 1):
            pheromones[route[i]][route[i + 1]] += 1.0 / cost

best_route, best_cost = aco_for_mTSP()

# Splitting the route for two robots (this section needs more elaborate design for a real mTSP solution)
midpoint = len(best_route) // 2
robot_0_route = [0] + best_route[:midavg_section] + [0]
robot_1_route = [1] + best_route[midpoint:] + [1]

robot_0_cost = calculate_total_cost(robot_0_route)
robot_1_cost = calculate_total_cost(robot_1_route)

print(f"Robot 0 Tour: {robot_0_route}")
print(f"Robot 0 Total Travel Cost: {robot_0_cost}")
print(f"Robot 1 Tour: {robot_1_route}")
print(f"Robot 1 Total Travel Cost: {robot_1_cost}")
print(f"Overall Total Travel Cost: {robot_0_cost + robot_1_cost}")