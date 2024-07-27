import numpy as np
import random

# Coordinates for each city including depots
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Number of cities and robots
num_cities = len(cities)
num_robots = 2

# Array to hold distances between each pair of cities
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i][j] = calculate_distance(i, j)

# Ant Colony Optimization parameters
antnum = 10
cyclenum = 100
alpha = 1.0     # influence of pheromone
beta = 5.0      # influence of heuristic visibility
rho = 0.1       # rate of pheromone evaporation
init_pheromone = 1.0 / num_cities

# Initialize pheromones
pheromones = np.full((num_cities, num_cities), init_pheromone)

def heuristic(i, j):
    """ Heuristic function, inverse of the distance """
    return 1.0 / distances[i][j] if distances[i][j] != 0 else 0

def update_pheromones(routes, costs):
    """ Update pheromone levels on the routes used by all ants """
    global pheromones
    pheromones *= (1 - rho)
    for i, route in enumerate(routes):
        contribution = 1.0 / costs[i]
        for j in range(len(route) - 1):
            pheromones[route[j], route[j + 1]] += contribution
            pheromones[route[j + 1], route[j]] += contribution  # Since the graph is undirected

def select_next_city(current_city, allowed_cities, pheromones, beta, alpha):
    """ Select the next city for an ant based on the transition probabilities """
    probabilities = []
    pheromone_list = pheromones[current_city]
    denominator = sum((pheromone_list[j]**alpha) * (heuristic(current_city, j)**beta) for j in allowed_cities)
    for j in allowed_cities:
        numerator = (pheromone_list[j]**alpha) * (heuristic(current_city, j)**beta)
        probabilities.append(numerator / denominator)
    return np.random.choice(allowed_cities, p=probabilities)

def construct_solution(route_start, pheromones, alpha, beta):
    """ Construct a tour for one ant starting from route_start """
    route = [route_start]
    allowed_cities = list(range(num_cities))
    allowed_cities.remove(route_start)
    
    current_city = route_start
    while allowed_cities:
        next_city = select_next_city(current_city, allowed_cities, pheromones, beta, alpha)
        route.append(next_city)
        allowed_cities.remove(next_city)
        current_city = next_city

    route.append(route_start)  # Return to depot
    return route

def calculate_route_cost(route):
    """ Calculate the total cost of a single route """
    return sum(distances[route[i], route[i+1]] for i in range(len(route) - 1))

# Main ACO algorithm
best_solution = None
best_cost = float('inf')

for cycle in range(cyclenum):
    routes = []
    costs = []
    for ant in range(antnum):
        if ant % num_robots == 0:
            start_city = 0  # Depot for robot 0
        else:
            start_city = 1  # Depot for robot 1
        route = construct_solution(start_city, pheromones, alpha, beta)
        cost = calculate_route_cost(route)
        routes.append(route)
        costs.append(cost)
    
    if sum(costs) < best_cost:
        best_solution, best_cost = routes, sum(costs)
    
    update_pheromones(routes, costs)

    # Print progress
    print(f"Cycle {cycle + 1}: Current Best Cost = {best_cost}")

# Optimal solutions and their costs
print("\nBest solutions and their costs:")
for robot_id in range(num_robots):
    route = best_solution[robot_id]
    cost = calculate_route_card(feedItem.getContent())
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")
print("\nOverall Total Travel Cost:", best_cost)