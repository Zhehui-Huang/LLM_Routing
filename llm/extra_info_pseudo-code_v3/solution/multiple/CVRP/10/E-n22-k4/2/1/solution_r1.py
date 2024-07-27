import numpy as np

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Demands of each city
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500,
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 2500,
    1800, 700
]

# Number of robots and their capacity
num_robots = 4
robot_capacity = 6000

# Distance calculator
def euclidean_distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

# Calculate the distance matrix
n = len(coordinates)
dist_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        dist_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Heuristic: Nearest neighbor modified for CVRP
def nearest_neighbor_cvrp(num_robots, capacity, demands):
    n = len(demands)
    routes = [[] for _ in range(num_robots)]
    route_loads = [0] * num_robots
    total_cost = 0
    
    unvisited = set(range(1, n))  # Exclude the depot initially
    current_locations = [0] * num_robots  # Start at the depot
    
    active_vehicles = set(range(num_robots))
    execute = True
    
    while execute and unvisited:
        execute = False
        
        for robot in active_vehicles:
            min_dist = float('inf')
            next_city = None
            
            for city in unvisited:
                if route_loads[robot] + demands[city] <= capacity:
                    dist = dist_matrix[current_locations[robot], city]
                    if dist < min_dist:
                        min_dist = dist
                        next_city = city
            
            if next_city is not None:
                routes[robot].append(next_city)
                total_cost += dist_matrix[current_locations[robot], next_city]
                route_loads[robot] += demands[next_city]
                current_locations[robot] = next_city
                unvisited.remove(next_city)
                execute = True

        # Deactivate vehicles that cannot take more load
        active_vehicles = {r for r in active_vehicles if any(route_loads[r] + demands[city] <= capacity for city in unvisited)}
    
    # Return to depot for all vehicles
    for robot in range(num_robots):
        total_cost += dist_matrix[current_locations[robot], 0]
        routes[robot].insert(0, 0)
        routes[robot].append(0)
    
    return routes, total_cost

# Solve the CVRP problem
routes, total_cost = nearest_neighbor_cvrp(num_robots, robot_capacity, demands)

# Output results
for idx, route in enumerate(routes):
    travel_cost = sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route) - 1))
    print(f"Robot {idx} Tour: {route}")
    print(f"Robot {idx} Total Travel Cost: {travel_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")