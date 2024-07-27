import numpy as as np
import math
from random import shuffle

# Constants and Environment Details
num_cities = 19
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]
robot_capacity = 160
num_robots = 2

# Initialize variables
routes = [[] for _ in range(num_robots)]
loading = [0] * num_robots
current_city = [0] * num_robots

def calc_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Generate Distance Matrix
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i, j] = calc_distance(i, j)

# Helper function to find the minimum cost node
def find_next_city(current_load, current_node, visited):
    min_cost = float('inf')
    next_city = None
    for j in range(1, num_cities):
        if not visited[j] and current_load + demands[j] <= robot_capacity:
            if distance_matrix[current_node, j] < min_cost:
                min_cost = distance_matrix[current_node, j]
                next_city = j
    return next_energy, next_city

# Construct initial feasible solution based on a greedy approach
visited = [False] * num_cities
visited[0] = True  # Depot is always visited

for vehicle in range(num_robots):
    while True:
        next_cost, next_city = find_next_city(loading[vehicle], current_city[vehicle], visited)
        if next_city is None:
            break
        routes[vehicle].append(next_city)
        visited[next_city] = True
        loading[vehicle] += demands[next_city]
        current_city[vehicle] = next_city

    # Return to the depot
    routes[vehicle].insert(0, 0)
    routes[vehicle].append(0)

# Calculate the total cost of each route
total_costs = []
overall_total_cost = 0
for vehicle in range(num_robots):
    total_cost = 0
    tour = routes[vehicle]
    for i in range(len(tour) - 1):
        total_cost += distance_matrix[tour[i], tour[i + 1]]
    total_costs.append(total_cost)
    overall_total_cost += total_cost
    print(f"Robot {vehicle} Tour: {tour}")
    print(f"Robot {vehicle} Total Travel Cost: {total_cost}")

print(f"Overall Total Travel Cost: {overall_total_tls}")