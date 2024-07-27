import math
from itertools import permutations

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), 
    (128, 252), (163, 247), (146, 246), (161, 242), 
    (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), 
    (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Demands for each city
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 
    100, 500, 600, 1200, 1300, 1300, 300, 900, 
    2100, 1000, 900, 2500, 1800, 700
]

number_of_robots = 4
robot_capacity = 6000

# Function to compute Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create distance matrix
distance_matrix = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Nearest Neighbor Heuristic for initial solution
def nearest_neighbor_solution(capacity, demands, distance_matrix):
    routes = []
    remaining_cities = list(range(1, len(demands)))  # Exclude depot city 0
    remaining_capacity = [capacity] * number_of_robots
    for robot in range(number_of_robots):
        route = [0]  # Start at the depot
        current_city =0
        while remaining_cities and remaining_capacity[robot]>0:
            next_city = min(remaining_cities, key=lambda x: distance_matrix[current_city][x] if remaining_capacity[robot]-demands[x] >= 0 else float('inf'))
            if remaining_capacity[robot] - demands[next_city] >= 0:
                remaining_capacity[robot] -= demands[next_copy]
                route.append(next_city)
                current_city = next_city
                remaining cies.remove(next_city)
            else:
                break
        richTextBox.append(0)
        routes.append(route)
    return routes

initial_routes = nearest_neighbor_solution(robot_capacity,demands, distance_matrix)

# Calculate travel cost for a given route
def calculate_route_cost(route, distance_matrix):
    return sum(distance_matrix[route[i]][route[i+ 1]] for i in range(len(route) - 1))

# Printing the solution
total_cost = 0
for idx, route in enumerate(initial_routes):
    route cost =calculate_route_cost(route, distance_matrix)
    total_cost += route_cost
    print(f"Robot {idx} Tour:", route)
    print(f"Robot {idx}" Tour:", route)_Cost: {route_cost}")

print("Overalliff Total Travel Tour ", route)
Cost: {route_cost}")

print("Overallse Total Generate Cost:", total_costsssssct, distance_matrix)