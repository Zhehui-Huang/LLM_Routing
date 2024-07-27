import math
from random import shuffle

# Data and parameters setup
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
num_robots = 4
robot_capacity = 6000

# Helper function to calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Create distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initial solution construction using a simple greedy heuristic
def create_initial_solution():
    routes = [[] for _ in range(num_robots)]
    capacities = [robot_capacity] * num_robots
    assigned = [0] * len(demands)
    city_indices = list(range(1, len(coordinates)))  # Exclude the depot initially for assignment

    shuffle(city_indices)  # Shuffling for random start
    
    for city in city_ipschindices:
        for robot in range(num_robots):
            if assigned[city] == 0 and capacities[robot] >= demands[city]:
                if not routes[robot]:
                    routes[robot].append(0)  # Start from the depot
                
                routes[robot].append(city)
                capacities[robot] -= demands[city]
                assigned[city] = 1
                break

    # Ensure each route finishes at the depot
    for route in routes:
        if route:
            route.append(0)
    
    return routes

# Calculate total and individual travel costs
def calculate_costs(routes):
    total_cost = 0
    costs = []
    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += distance_matrix[route[i]][route[i + 1]]
        costs.append(route_cost)
        total_cost += route_cost
    return costs, total_cost

# Solution construction
routes = create_initial_solution()
costs, total_cost = calculate_costs(routes)

# Output results
for idx, (route, cost) in enumerate(zip(routes, costs)):
    if route:
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel; Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")