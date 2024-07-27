from math import sqrt
import random

# Given data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

num_robots = 2
robot_capacity = 160

# Calculate Euclidean distance between two points
def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Precompute distances
dist_matrix = [[distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Attempt to divide cities based on nearest to depot sorting and demand
def initial_solution():
    city_indices = list(range(1, len(coordinates)))
    city_indices.sort(key=lambda x: dist_matrix[0][x])  # Sort cities based on proximity to depot

    routes = [[] for _ in range(num_robots)]
    capacities = [robot_capacity for _ in range(num_robots)]
    
    for city in city_indices:
        # Assign city to the robot with enough remaining capacity and nearest to the last assigned city in the route
        best_robot = None
        min_additional_cost = float('inf')
        for robot_id in range(num_robots):
            if capacities[robot_id] >= demands[city]:
                if routes[robot_id]:
                    last_city = routes[robot_id][-1]
                else:
                    last_city = 0  # Start from depot
                cost = dist_matrix[last_city][city]
                if cost < min_additional_cost:
                    min_additional_cost = cost
                    best_robot = robot_id
        
        if best_robot is not None:
            routes[best_robot].append(city)
            capacities[best_robot] -= demands[city]
    
    # Complete the routes by returning to the depot
    for route in routes:
        route.insert(0, 0)  # start at depot
        route.append(0)     # end at depot
        
    return routes

def calculate_route_cost(route):
    return sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

# Generate initial solution and calculate its cost
routes = initial_solution()
total_cost = 0

for i, route in enumerate(routes):
    rcost = calculate_route_cost(route)
    total_cost += rcost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {rcost}")

print(f"Overall Total Travel Cost: {total_cost}")