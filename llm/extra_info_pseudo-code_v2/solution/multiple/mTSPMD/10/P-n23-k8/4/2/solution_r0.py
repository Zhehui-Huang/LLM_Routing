import numpy as np
import math

# City information
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Robot information
robot_depot = {
    i: i for i in range(8)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + 
                     (city_coords[city1][1] - city_coords[city2][1])**2)

def initialize_pheromone_matrix(n, initial_pheromone):
    return np.full((n, n), initial_pheromone)

def calculate_transition_probabilities(pheromone_mat, heuristic_mat, alpha, beta, allowed):
    total = sum((pheromone_mat[current][j]**alpha) * (heuristic_mat[current][j]**beta) for j in allowed)
    probabilities = [(pheromone_mat[current][j]**alpha) * (heuristic_mat[current][j]**beta) / total for j in allowed]
    return probabilities

def construct_solutions(robots, num_cities, pheromone_mat, heuristic_mat, alpha, beta):
    routes = {robot: [robot_depot[robot]] for robot in robots}
    to_visit = set(range(num_cities)) - set(robot_depot.values())

    for robot in robots:
        current = robot_depot[robot]
        while to_visit:
            allowed = list(to_visit)
            if not allowed:
                break
            probabilities = calculate_transition_probabilities(pheromone_mat, heuristic_mat, alpha, beta, allowed)
            next_city = np.random.choice(allowed, p=probabilities)
            routes[robot].append(next_city)
            to_visit.remove(next_city)
            current = next_city
        routes[robot].append(robot_depot[robot])  # Return to depot

    return routes

def update_pheromone(pheromone_mat, route, rho, Q):
    for i in range(len(route) - 1):
        pheromone_mat[route[i]][route[i+1]] *= (1 - rho)
        pheromone_mat[route[i]][route[i+1]] += Q

def calculate_route_length(route):
    return sum(euclidean_distance(route[i], route[i+1]) for i in range(len(route) - 1))

def ant_colony_optimization():
    np.random.seed(0)
    num_cities = len(city_coords)
    robots = robot_depot.keys()
    
    alpha = 1.0
    beta = 2.0
    rho = 0.1
    Q = 100
    cyclenum = 100
    initial_pheromone = 1.0
    pheromone_mat = initialize_pheromone_matrix(num_cities, initial_pheromone)
    heuristic_mat = [[1 / (euclidean_distance(i, j) if i != j else 1e-10) for j in range(num_cities)] for i in range(num_cities)]

    best_solution = None
    best_total_cost = float('inf')
    
    for _ in range(cyclenum):
        solutions = construct_solutions(robots, num_cities, pheromone_mat, heuristic_mat, alpha, beta)
        for robot, route in solutions.items():
            update_pheromone(pheromone_mat, route, rho, Q)

        # Assess the solution
        total_cost = sum(calculate_route_length(route) for route in solutions.values())
        if total_cost < best_total_cost:
            best_solution = solutions
            best_total_cost = total_cost

    # Output results
    overall_cost = 0
    for robot, route in best_solution.items():
        cost = calculate_route_length(route)
        overall_cost += cost
        print(f"Robot {robot} Tour: {route}")
        print(f"Robot {robot} Total Travel Cost: {cost:.2f}")
    
    print(f"Overall Total Travel Copper COOKIE: {overall_cost:.2f}")

ant_colony_optimization()