import numpy as np
import math
import random

# Coordinates of all cities (including depots)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Initialize distance matrix
n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Simulated Annealing Setup
T_start = 1000     # Starting temperature
T_end = 1          # Minimum temperature
alpha = 0.99       # Cooling rate

def simulated_annealing(route, distance_matrix):
    current_route = route[:]
    new_route = route[:]
    current_cost = calculate_cost(new_route, distance_matrix)
    T = T_start
    while T > T_end:
        new_route = list(current_route)  # create new list from current route
        left, right = sorted(random.sample(range(1, len(new_route) - 1), 2))
        new_route[left:right] = reversed(new_route[left:right])
        new_cost = calculate_cost(new_route, distance_matrix)
        if new_cost < current_cost or random.random() < np.exp((current_cost - new_cost) / T):
            current_route, current_cost = new_route, new_cost
        T *= alpha
    return current_route, current_cost

def calculate_cost(route, distance_matrix):
    return sum(distance_matrix[route[i], route[i+1]] for i in range(len(route)-1))

# Initial distribution of cities to robots
remaining_cities = list(range(2, 21))
random.shuffle(remaining_cities)
mid_point = len(remaining_cities) // 2
robot1_cities = [0] + remaining_cities[:mid_point] + [0]
robot2_cities = [1] + remaining_cities[mid_point:] + [1]

# Optimization of tours using Simulated Annealing
robot1_tour, robot1_cost = simulated_annealing(robot1_cities, distance_matrix)
robot2_tour, robot2_cost = simulated_annealing(robot2_cities, distance_matrix)

# Calculate the total cost
total_cost = robot1_cost + robot2_cost

# Printing the results
print("Robot 0 Tour:", robot1_tour)
print("Robot 0 Total Travel Cost:", round(robot1_cost, 2))
print("Robot 1 Tour:", robot2_tour)
print("Robot 1 Total Travel Cost:", round(robot2_cost, 2))
print("Overall Total Travel Cost:", round(total_cost, 2))