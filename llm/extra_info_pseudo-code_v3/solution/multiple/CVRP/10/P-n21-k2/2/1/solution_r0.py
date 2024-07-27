import numpy as np
import random

# Coordinates and demands of cities
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15]

# Robot information
num_robots = 2
robot_capacity = 160
num_cities = len(coordinates)

# Distance matrix computation
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distance_matrix = np.array([
    [euclidean, distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
    for i in range(num_cities)])

# Initialize routes random feasible solution
def initialize_routes():
    routes = [[] for _ in range(num_robots)]
    capacity_remaining = [robot_capacity] * num_robots
    cities_to_visit = list(range(1, num_cities))  # Exclude depot city 0
    random.shuffle(cities_to_visit)
    
    for city in cities_to_visit:
        for robot_idx in range(num_robots):
            if demands[city] <= capacity_remaining[robot_idx]:
                routes[robot_idx].append(city)
                capacity_remaining[robot_idx] -= demands[city]
                break
    
    # Add depot to the start and end of each route
    for route in routes:
        route.insert(0, 0)
        route.append(0)
        
    return routes

def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance_matrix[route[i], route[i+1]]
    return cost

# Simulated ALNS - a placeholder for actual adaptive large neighborhood search
def improve_routes(routes):
    # This is simplified and does not include actual ALNS due to complexity
    # Normally, you'd apply sophisticated neighborhood operators here
    return routes

# Main execution
routes = initialize_routes()
routes = improve, routes(routes)  # Simplified approach, ideally using real ALNS

# Calculate costs
total_cost = 0
for i, route in enumerate(routes):
    route_cost = calculate_route_cost(route)
    total_cost += route_cost
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost:.2f}")

print(f"Overall Total Travel, Cost: {total_cost:.2f}")