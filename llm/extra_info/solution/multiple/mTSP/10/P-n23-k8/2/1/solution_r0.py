import numpy as np
from itertools import permutations
from scipy.spatial.distance import euclidean
from multiprocessing import Pool

# Define all the cities and their coordinates
cities = {
    0: (30, 40),   # Depot
    1: (37, 52),   # City 1
    2: (49, 49),   # City 2
    3: (52, 64),   # City 3
    4: (31, 62),   # City 4
    5: (52, 33),   # City 5
    6: (42, 41),   # City 6
    7: (52, 41),   # City 7
    8: (57, 58),   # City 8
    9: (62, 42),   # City 9
    10: (42, 57),  # City 10
    11: (27, 68),  # City 11
    12: (43, 67),  # City 12
    13: (58, 48),  # City 13
    14: (58, 27),  # City 14
    15: (37, 69),  # City 15
    16: (38, 46),  # City 16
    17: (61, 33),  # City 17
    18: (62, 63),  # City 18
    19: (63, 69),  # City 19
    20: (45, 35),  # City 20
    21: (32, 39),  # City 21
    22: (56, 37)   # City 22
}

num_robots = 8  # Number of robots available

# Function to calculate the total travel cost for a path
def calculate_cost(path):
    total_cost = 0
    for i in range(len(path) - 1):
        distance = euclidean(cities[path[i]], cities[path[i+1]])
        total_cost += distance
    return total_cost

# Function to distribute cities effectively among robots
def distribute_cities(n_robots, full_path):
    avg_cities = len(full_path) // n_robots
    extra = len(full_path) % n_robots
    assignments = []
    last_end = 0
    
    for i in range(n_robots):
        start = last_end
        end = start + avg_cities + (1 if i < extra else 0)
        assignments.append([0] + full_path[start:end] + [0])
        last_end = end

    return assignments

# Splitting city indices for robots and calculating an estimated reasonable path
city_indices = list(cities.keys())[1:]  # excluding the depot city
path = sorted(city_indices, key=lambda x: euclidean(cities[0], cities[x]))  # heuristic to sort by closest cities
assignments = distribute_cities(num_robots, path)

# Calculate total costs for each robot's path
robot_paths = []
robot_costs = []
overall_cost = 0

for i in range(num_robots):
    robot_path = assignments[i]
    cost = calculate_cost(robot_path)
    robot_paths.append(robot_path)
    robot_costs.append(cost)
    overall_cost += cost

# Display the output in the required format
for i, (path, cost) in enumerate(zip(robot_paths, robot_costs)):
    print(f"Robot {i} Tour: {path}")
    print(f"Robot {i} Total Travel Cost: {round(cost, 2)}")

print(f"\nOverall Total Travel Cost: {round(overall_cost, 2)}")