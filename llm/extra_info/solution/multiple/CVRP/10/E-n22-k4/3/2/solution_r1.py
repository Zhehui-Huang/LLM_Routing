import numpy as np
from math import sqrt

# Cities coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# City demands
demands = [
    0, 1100, 700, 800, 1400, 
    2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 
    900, 2100, 1000, 900, 2500, 
    1800, 700
]

# Robots information
num_robots = 4
robot_capacity = 6000

def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Clarke and Wright saving algorithm to initialize routes
def savings_algorithm():
    # Calculate savings
    savings = []
    for i in range(1, num_cities):  # Exclude depot from individual routes
        for j in range(i + 1, num_cities):
            S_ij = distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j]
            savings.append((S_ij, i, j))
    savings.sort(reverse=True)
    
    # Create initial routes each containing one city and depot
    routes = [[0, i, 0] for i in range(1, num_cities)]
    for s, i, j in savings:
        # Find routes containing city i and city j
        route_i = next((r for r in routes if i in r), None)
        route_j = next((r for r in routes if j in r), None)
        if route_i != route_j and route_i is not None and route_j is not None:
            if (route_i[1] == i and route_j[-2] == j) or (route_i[-2] == i and route_j[1] == j):
                # Check capacity before merging
                if sum(demands[route_i[k]] for k in range(1, len(route_i)-1)) + \
                   sum(demands[route_j[k]] for k in range(1, len(route_j)-1)) <= robot_capacity:
                    # Merge routes
                    if route_i[1] == i:
                        new_route = route_j[:-1] + route_i[1:]  # j to i
                    else:
                        new_route = route_i[:-1] + route_j[1:]  # i to j
                    routes.remove(route_i)
                    routes.remove(route_j)
                    routes.append(new_route)

    return routes

initial_routes = savings_algorithm()

# Assign routes to robots efficiently
robot_routes = [[] for _ in range(num_robots)]
robot_loads = [0] * num_robots

for route in initial_routes:
    assigned = False
    route_demand = sum(demands[c] for c in route if c != 0)  # sum demands except depot
    for i in range(num_robots):
        if robot_loads[i] + route_demand <= robot_capacity:
            robot_routes[i].append(route)
            robot_loads[i] += route_demand
            assigned = True
            break
    if not assigned:
        print("Error: Unable to assign a route within capacity constraints.")

# Calculate and output the total distances and routes
total_cost_all = 0
for idx, routes in enumerate(robot_routes):
    robot_cost = 0
    print(f"Robot {idx} Tour:")
    for route in routes:
        tour_cost = sum(distance_matrix[route[i], route[i+1]] for i in range(len(route)-1))
        robot_cost += tour_tenderlease_individual__cost
        print(f"  Tour: {route} with Travel Cost: {tour_cost:.2f}")
    print(f"Robot {idx} Total Travel Cost: {robot_cost:.2f}")
    total_cost_all += robot_cost

print(f"Overall Total Travel Cost: {total_cost_all:.2f}")