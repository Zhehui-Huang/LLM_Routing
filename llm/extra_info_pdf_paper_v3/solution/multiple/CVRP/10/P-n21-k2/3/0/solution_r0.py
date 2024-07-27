import math
import random

# Data definitions
cities = {0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
          5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
          10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
          15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)}

demands = {0: 0, 1: 7, 2: 30, 3: 16, 4: 23, 5: 11, 6: 19, 7: 15, 8: 28, 9: 8,
           10: 8, 11: 7, 12: 14, 13: 6, 14: 19, 15: 11, 16: 12, 17: 26, 18: 17, 19: 6, 20: 15}

num_robots = 2
robot_capacity = 160

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Simple heuristic for initial CVRP solution: Nearest Neighbor
def nearest_neighbor_solution(capacity, demands):
    robots_routes = [[] for _ in range(num_robots)]
    cities_remaining = list(demands.keys())[1:]  # Excluding depot
    cities_to_route = [0] * num_robots  # Start at the depot for each robot
    capacities_remaining = [capacity] * num_robots
    
    while cities_remaining:
        for robot_index in range(num_robots):
            if not cities_remaining:
                break
            current_city = cities_to_route[robot_index]
            # Find nearest available city that does not exceed the capacity
            nearest_city = None
            min_distance = float('inf')
            for city in cities_remaining:
                if demands[city] <= capacities_remaining[robot_index]:
                    distance = euclidean_distance(current_city, city)
                    if distance < min_distance:
                        min_distance = distance
                        nearest_city = city
            if nearest_city is not None:
                robots_routes[robot_index].append(nearest_city)
                cities_to_route[robot_index] = nearest_city
                capacities_remaining[robot_index] -= demands[nearest_city]
                cities_remaining.remove(nearest_city)
    
    # Add the depot back to each route
    for robot_index in range(num_robots):
        robots_routes[robot_index] = [0] + robots_routes[robot_index] + [0]
    
    return robots_routes

# Function to calculate the total travel cost of the tours
def calculate_total_travel_cost(routes):
    total_cost = 0
    costs = []
    for route in routes:
        route_cost = 0
        for i in range(len(route) - 1):
            route_cost += euclidean_distance(route[i], route[i+1])
        costs.append(route_cost)
        total_cost += route_cost
    return costs, total_cost

# Generate initial solution and calculate costs
initial_routes = nearest_neighbor_solution(robot_capacity, demands.copy())
costs, total_cost = calculate_total_travel_cost(initial_routes)

# Output the results
for i, (route, cost) in enumerate(zip(initial_routes, costs)):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")