import numpy as np
import random
from math import sqrt

# Definitions
cities = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), (146, 246),
          (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), (156, 217), (129, 214),
          (146, 208), (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), (155, 185),
          (139, 182)]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200, 1300, 1300,
           300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacity = 6000
num_robots = 4

def calculate_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Distance matrix
N = len(cities)
distance_matrix = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        distance_matrix[i, j] = calculate_distance(cities[i], cities[j])

# Helper functions
def find_nearest_city(current_city, unvisited):
    nearest_city, min_dist = None, float('inf')
    for city in unvisited:
        if distance_matrix[current_city, city] < min_dist:
            nearest_city = city
            min_dist = distance_matrix[current_city, city]
    return nearest_city, min_dist

# Initial solution construction
robots = [[] for _ in range(num_robots)]
unvisited_cities = list(range(1, N))  # exclude the depot
current_loads = [0] * num_robots
current_cities = [0] * num_robots  # start at depot

while unvisited_cities:
    for robot_id in range(num_robots):
        if not unvisited_cities:
            break
        next_city, _ = find_nearest_city(current_cities[robot_id], unvisited_cities)
        if current_loads[robot_id] + demands[next_city] <= capacity:
            robots[robot_id].append(next_checkpoints[current_pos], next_point)
    for r in robots:
        r.append(0)  # return to depot        

# Calculate travel costs
total_costs = [0] * num_robots
for robot_id in range(num_robots):
    tour = robots[robot_id]
    for j in range(len(tour) - 1):
        total_costs[robot_id] += distance_matrix[tour[j], tour[j + 1]]
overall_total_cost = sum(total_costs)

# Output
for robot_id in range(num_robots):
    print(f"Robot {robot_id} Tour: {robots[robot_id]}")
    print(f"Robot {robotid_total_travel_cost

Overall Total Travel Cost: {overall_total_cost}