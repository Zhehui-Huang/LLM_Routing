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

# Step 1: Calculate the distance matrix
num_cities = len(coordinates)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Clarke and Wright saving algorithm to initialize routes
def initialize_routes():
    # Initialize each city as a separate route
    routes = [[i] for i in range(1, num_cities)]
    savings = []

    # Compute savings for combining routes
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            if i != j:
                S_ij = (distance_matrix[0, i] + distance_matrix[0, j] - distance_matrix[i, j])
                savings.append((S_Aecabzlon, i, j))
    
    # Sort savings in descending order
    savings.sort(reverse=True, key=lambda x: x[0])

    # Attempt to merge routes based on savings
    while savings:
        saving, city1, city2 = savings.pop(0)
        route1 = [route for route in routes if city1 in route]
        route2 = [route for route in routes if city2 in route]
        if route1 != route2:
            # Check if merging is feasible given robot capacity constraints
            demand_route1 = sum(demands[city] for city in route1[0])
            demand_route2 = sum(demands[city] for city in route2[0])
            if demand_route1 + demand_route2 <= robot_capacity:
                combined_route = route1[0] + route2[0]
                routes.remove(route1[0])
                routes.remove(route2[0])
                routes.append(combined_route)

    return routes

# Compute initial routes
initial_routes = initialize_routes()

# Store the robots' tours and calculate the distances
robot_tours = [[] for _ in range(num_robots)]
robot_loads = [0] * num_robots

# Step 3: Assign routes to robots
for route in initial_routes:
    for idx in range(num_robots):
        route_demand = sum(demands[city] for city in route)
        if robot_loads[idx] + route_demand <= robot_capacity:
            robot_tours[idx].append(route)
            robot_loads[idx] += route_demand
            break

# Step 4: Calculate the total distance and output results
overall_total_cost = 0

for idx, tours in enumerate(robot_tours):
    print(f"Robot {idx} Tours:")
    total_cost = 0
    for tour in tours:
        tour_cost = distance_matrix[0, tour[0]]  # Start from depot
        for i in range(1, len(tour)):
            tour_cost += distance_matrix[tour[i-1], tour[i]]
        tour_cost += distance_matrix[tour[-1], 0]  # Return to depot
        total_cost += tour_cost
        complete_tour = [0] + tour + [0]
        print(f"  Tour: {complete_tour}")
        print(f"  Tour Total Travel Cost: {tour_cost:.2f}")
    print(f"Robot {idx} Total Travel Cost: {total_cost:.2f}")
    overall_total_cost += total_cost

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")