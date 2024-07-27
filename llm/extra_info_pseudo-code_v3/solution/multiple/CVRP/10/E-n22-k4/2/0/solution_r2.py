import math
import random

# Coordinates of cities including the depot
cities = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Demand of each city excluding the depot
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300,
    300, 900, 2100, 1000, 900, 2500, 1800, 700
]

# Constants
num_robots = 4
robot_capacity = 6000
depot = 0

def calc_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def construct_initial_solution():
    robots = [[] for _ in range(num_robots)]
    city_indices = list(range(1, len(cities)))  # Exclude depot
    random.shuffle(city_indices)
    current_loads = [0] * num_robots

    for city in city_indices:
        for robot_index in range(num_robots):
            if current_loads[robot_index] + demands[city] <= robot_capacity:
                robots[robot_index].append(city)
                current_loads[robot_index] += demands[city]
                break

    # Add depot at the start and end of each route
    for robot_index in range(num_robots):
        robots[robot_index] = [depot] + robots[robot_index] + [depot]

    return robots

def calculate_route_cost(route):
    cost = 0
    for i in range(1, len(route)):
        cost += calc_distance(cities[route[i - 1]], cities[route[i]])
    return cost

# Heuristic: Simple initial solution constructor
initial_routes = construct_initial_solution()

# Printing results
overall_cost = 0
for i, route in enumerate(initial_routes):
    if route:  # Calculate and print if route is not empty
        route_cost = calculate_route_cost(route)
        overall_cost += route_cost
        print(f"Robot {i} Tour: {route}")
        just_route_cost_cost = f"{route_cost:.2f}"
        print(f"Robot {itore_cost_cost}")

print(f"Overallaris Total Feel	entSysOverall Travel Tent: $ {above_Coverall_costs}:.2fs If")TO