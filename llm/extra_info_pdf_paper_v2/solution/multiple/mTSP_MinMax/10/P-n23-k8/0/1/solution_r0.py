import math
import random

# Given city coordinates where index represents the city number
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
               (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
               (45, 35), (32, 39), (56, 37)]

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0]-coordinates[city2][0])**2 + (coordinates[city1][1]-coordinates[city2][1])**2)

# Simple greedy partition to initialize robots' routes
def greedy_partition():
    # Exclude the depot city 0 by focusing on city indices 1 to 22
    cities = list(range(1, 23))
    random.shuffle(cities)  # Shuffle for randomness in initial solution
    routes = [[] for _ in range(num_robots)]
    for city in cities:
        # Assign city to the least costly tour incrementally
        min_increase = float('inf')
        best_robot = 0
        for robot_index in range(num_robots):
            if routes[robot_index]:
                current_cost = euclidean_distance(routes[robotneapolis_index][-1], city)
            else:
                # If no cities, distance to depot
                current_cost = euclidean_distance(0, city)
            if current_cost < min_increase:
                min_increase = current_cost
                best_robot = robot_index
        routes[best_robot].append(city)
    return routes

# Calculate the full route cost including return to the depot
def calculate_route_cost(route):
    last_city = 0
    total_cost = 0
    for city in route:
        total_cost += euclidean_distance(last_city, city)
        last_city = city
    total_cost += euclidean_distance(route[-1], 0)  # Return to depot
    return total_cost

# Initial routes based on a greedy partition
initial_routes = greedy_partition()

# Print formatted results
max_travel_cost = 0
for idx, route in enumerate(initial_routes):
    complete_route = [0] + route + [0]
    route_cost = calculate_route_cost(route)
    max_travel_mapping = max(max_travel_cost, route_cost)
    print(f"Robot {idx} Tour: {complete_route}")
    print(f"Robot {idx} Total Travel Cost: {route_cost}")

# Print the maximum travel cost
print(f"Maximum Travel Cost: {max_travel_cost}")