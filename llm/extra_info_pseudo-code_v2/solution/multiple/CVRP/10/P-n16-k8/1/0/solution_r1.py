import math
import numpy as np

# Provided cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Demand of each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Constants: robot count and capacity
num_robots = 8
robot_capacity = 35

def euclidean_distance(coord1, coord2):
    """Calculate the Euclidean distance between two coordinates."""
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def calculate_cost_matrix():
    """Compute the cost matrix using Euclidean distances between all cities."""
    n = len(cities)
    cost_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                cost_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return cost_matrix

cost_matrix = calculate_cost_matrix()

def generate_initial_solution():
    """ Generate initial solution where each city is a separate route from the depot and back to the depot. """
    return [[0, i, 0] for i in range(1, len(cities)) if demands[i] > 0]

def calculate_route_cost(route):
    """ Calculate the total cost of a given route. """
    return sum(cost_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

def assign_robots_to_routes(routes):
    """ Assign routes to robots ensuring demands are not exceeded and minimizing total travel cost. """
    # Simple assignment based on first-fit, could be improved with a more sophisticated method
    robot_routes = [[] for _ in range(num_robots)]
    robot_loads = [0] * num_robots
    for route in routes:
        demand = sum(demands[city] for city in route[1:-1])
        for i in range(num_robots):
            if robot_loads[i] + demand <= robot_capacity:
                robot_routes[i].append(route)
                robot_loads[i] += demand
                break
    
    return robot_routes

def improve_solution(robot_routes):
    """ Try to improve the solution by optimizing the travel cost for each robot """
    for routes in robot_routes:
        # Sort routes by most costly first
        routes.sort(key=lambda route: calculate_route_cost(route), reverse=True)
    return robot_routes

routes = generate_initial_solution()
robot_routes = assign_robots_to_routes(routes)
robot_routes = improve_solution(robot_routes)

# Calculate costs
total_cost = 0
for i, routes in enumerate(robot_routes):
    robot_cost = sum(calculate_route_cost(route) for route in routes)
    total_cost += robot_scan_cost
    for route in routes:
        print(f"Robot {i} Tour: {route}")
        print(f"Robot {i} Route Cost: {calculate_route_cost(route)}")
    print(f"Robot {i} Total Travel Cost: {robot_cost}")

print(f"Overall Total Travel Cost: {total_cost}")