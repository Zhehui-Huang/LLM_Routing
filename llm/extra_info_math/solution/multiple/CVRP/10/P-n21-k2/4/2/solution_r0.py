import math
from itertools import permutations

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# City demands
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12,
    26, 17, 6, 15
]

# Robot data
num_robots = 2
robot_capacity = 160

# Compute the Euclidean distance between two locations
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
def create_distance_matrix(coords):
    n = len(coords)
    dist_matrix = [[calculate_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]
    return dist_matrix

# Clarke-Wright Savings Algorithm implementation for multiple robots
def clark_wright(routes, capacity, demands, dist_matrix):
    def saving(i, j):
        return dist_matrix[0][i] + dist_matrix[0][j] - dist_matrix[i][j]
    
    n = len(dist_matrix)
    savings = [(saving(i, j), i, j) for i in range(1, n) for j in range(1, n) if i != j]
    savings.sort(reverse=True, key=lambda x: x[0])  # Maximize savings
    
    while savings:
        _, i, j = savings.pop(0)
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        
        if route_i != route_j:
            if route_i is None:
                route_i = [0, i, 0]
                routes.append(route_i)
            if route_j is None:
                route_j = [0, j, 0]
                routes.append(route_j)
            
            # Combine routes if capacities allow
            if route_i[1:] + route_j[1:-1]:
                combined_demand = sum(demands[k] for k in route_i[1:-1] + route_j[1:-1])
                
                if combined_demand <= capacity:
                    route_i.pop()
                    route_i.extend(route_j[1:])
                    routes.remove(route_j)
    
    return routes

# Initialize single routes from depot to each city and back
initial_routes = [[0, i, 0] for i in range(1, len(coordinates))]

# Calculate distance matrix
distance_matrix = create_distance_matrix(coordinates)

# Divide initial routes among robots, trying to keep total demand close to capacity
assigned_routes = [[] for _ in range(num_robots)]

for route in initial_routes:
    assigned_demand = [sum(demands[city] for city in ro if city != 0) for ro in assigned_routes]
    least_loaded_robot = assigned_demand.index(min(assigned_demand))
    assigned_routes[least_loaded_robot].append(route)

# Compute optimized routes for each robot
optimized_routes = []
for initial_route in assigned_routes:
    optimized_routes.append(clark_wright(initial_route, robot_capacity, demands, distance_matrix))

# Calculate and display routes with total travel costs
total_cost = 0

for idx, routes in enumerate(optimized_routes):
    for route in routes:
        tour_cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
        print(f"Robot {idx} Tour: {route}")
        print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")
        total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")