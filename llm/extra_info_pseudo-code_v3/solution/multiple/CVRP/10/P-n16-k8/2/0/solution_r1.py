import numpy as np
from math import sqrt

# Given data
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]
num_robots = 8
robot_capacity = 35

# Distance matrix calculation
def euclidean(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

distance_matrix = np.array([[euclidean(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))])

# Initialize tours for each robot
routes = {i: [0] for i in range(num_robots)}  # each robot starts at depot
current_loads = {i: 0 for i in range(num_robots)}
remaining_cities = set(range(1, len(coordinates)))

while remaining_cities:
    for i in range(num_robots):
        if not remaining_cities:
            break
        possible_cities = [city for city in remaining_cities if current_loads[i] + demands[city] <= robot_capacity]
        if possible_cities:
            chosen_city = min(possible_cities, key=lambda x: distance_matrix[routes[i][-1]][x])
            routes[i].append(chosen_city)
            current_loads[i] += demands[chosen_city]
            remaining_cities.remove(chosen_city)

# Making sure each robot returns to the depot
for i in range(num_robots):
    routes[i].append(0)

# Calculate route costs
def calculate_route_cost(route, dist_matrix):
    return sum(dist_matrix[route[i]][route[i+1]] for i in range(len(route)-1))

# Print and calculate costs
total_cost = 0
for i in range(num_robots):
    cost = calculate_route_cost(routes[i], distance_matrix)
    print(f"Robot {i} Tour: {routes[i]}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")
    total_cost += cost

print(f"Overall Total Travel Cost: {total_cost:.2f}")