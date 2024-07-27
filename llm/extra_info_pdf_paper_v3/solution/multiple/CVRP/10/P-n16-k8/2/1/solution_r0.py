import math
import random
from collections import defaultdict

# Define city coordinates and demands
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]
city_demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Parameters
num_robots = 8
robot_capacity = 35
num_cities = len(city_coordinates)

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = city_coordinates[city1]
    x2, y2 = city_coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Seed for reproducibility in randomness
random.seed(0)

# Initial greedy solution for routes
def create_initial_solution():
    remaining_cities = set(range(1, num_cities))  # excluding depot
    routes = []
    for _ in range(num_robots):
        load = 0
        route = [0]  # start at depot
        while remaining_cities and load < robot_capacity:
            last_city = route[-1]
            next_city = min(remaining_cities, key=lambda city: distance(last_city, city) if city_demands[city] + load <= robot_capacity else float('inf'))
            demand = city_demands[next_city]
            if load + demand > robot_capacity:
                break
            route.append(next_city)
            load += demand
            remaining_cities.remove(next_city)
        route.append(0)  # return to depot
        routes.append(route)
    return routes

# Calculate the total travel cost of a route (start and end at depot)
def calculate_route_cost(route):
    cost = 0
    for i in range(len(route) - 1):
        cost += distance(route[i], route[i+1])
    return cost

# Assign an initial feasible solution
routes = create_initial_solution()
route_costs = [calculate_route_cost(route) for route in routes]
overall_cost = sum(route_costs)

# Output results
for i, route in enumerate(routes):
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_costs[i]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")