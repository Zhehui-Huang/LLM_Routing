import numpy as np
from scipy.spatial.distance import euclidean

# City coordinates and demands
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600,
           1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]

# Robot information
num_robots = 4
robot_capacity = 6000

# Create distance matrix
def create_distance_matrix(coords):
    num_cities = len(coords)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            dist_matrix[i, j] = euclidean(coords[i], coords[j])
    return dist_matrix

dist_matrix = create_distance_matrix(coordinates)

# CVRP solver using a straightforward greedy construction heuristics
def simple_cvrp_solver(demands, capacity, num_robots, distance_matrix):
    num_cities = len(demands)
    routes = []
    demands_remaining = demands[:]
    vehicle_routes = {i: [0] for i in range(num_robots)}
    load = {i: 0 for i in range(num_robots)}
    total_cost = 0

    # Assign cities to vehicles
    for v in range(num_robots):
        current_city = 0
        while any(demands_remaining[1:]):
            next_city = None
            min_dist = float('inf')
            for j in range(1, num_cities):
                if demands_remaining[j] > 0 and load[v] + demands_remaining[j] <= capacity:
                    if distance_matrix[current_city][j] < min_dist:
                        min_dist = distance_matrix[current_city][j]
                        next_city = j
            if next_city is None:
                break
            vehicle_routes[v].append(next_city)
            load[v] += demands_remaining[next_city]
            demands_remaining[next_index] = 0
            current_city = next_index
        
        vehicle_routes[v].append(0)
        route_cost = sum(distance_matrix[vehicle_routes[v][i]][vehicle_routes[v][i+1]] for i in range(len(vehicle_routes[v]) - 1))
        total_cost += route_cost
        routes.append((vehicle_routes[v], route_cost))

    return routes, total_cost

# Solve CVRP
routes, total_cost = simple_cvrp_solver(demands, robot_capacity, num_robots, dist_matrix)

# Output the tours for each robot
for index, (route, cost) in enumerate(routes):
    print(f"Robot {index} Tour: {route}")
    print(f"Robot {index} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")