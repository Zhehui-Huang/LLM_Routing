import numpy as np
import math

# Data definition
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Define robot depots
robot_depot = {i: i for i in range(8)}

def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + 
                     (city_coords[city1][1] - city_coords[city2][1])**2)

def initialize_pheromone_matrix(n, initial_pheromone):
    return np.full((n, n), initial_pheromone)

def calculate_transition_probabilities(pheromone_mat, heuristic_mat, alpha, beta, current, allowed):
    total = sum((pheromone_mat[current][j]**alpha) * (heuristic_mat[current][j]**beta) for j in allowed)
    probabilities = [(pheromone_mat[current][j]**alpha) * (heuristic_mat[current][j]**beta) / total for j in allowed]
    return np.array(probabilities)

def ant_colony_optimization():
    num_cities = len(city_coords)
    robots = robot_depot.keys()
    
    alpha = 1.0
    beta = 2.0
    rho = 0.1
    initial_pheromone = 1.0 / num_cities
    pheromone_mat = initialize_pheromone_matrix(num_cities, initial_pheromone)
    heuristic_mat = np.array([[1 / euclidean_distance(i, j) if i != j else float('inf') for j in range(num_cities)] for i in range(num_cities)])
    
    iterations = 100
    best_total_cost = float('inf')
    best_solution = None

    for iteration in range(iterations):
        routes = {robot: [robot_depot[robot]] for robot in robots}
        for robot in robots:
            unvisited = set(range(num_cities)) - {robot_depot[robot]}
            current = robot_depot[robot]

            while unvisited:
                allowed = list(unvisited)
                probabilities = calculate_transition_probabilities(pheromone_mat, heuristic_mat, current, allowed, alpha, beta)
                next_city = np.random.choice(allownumerusformTesting components in isolated or production-like environments can help identify such missing relational dynamics. To further investigate and address your concern, I'm presenting an improved version of the complete function with the necessary output statements re-added to ensure the tour and travel cost information is displayed.