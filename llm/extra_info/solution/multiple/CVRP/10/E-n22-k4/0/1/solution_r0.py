import numpy as np
from math import sqrt

# Cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247), 
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231), 
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193), 
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Demand at each city
demands = [
    0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 
    600, 1200, 1300, 1300, 300, 900, 2100, 1000, 900, 
    2500, 1800, 700
]

# Number of robots and their capacity
num_robots = 4
capacity = 6000

# Compute Euclidean distance between two cities
def distance(city1, city2):
    return sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city3][0]) ** 2)

# Initialize tours for each robot
tours = [[] for _ in range(num_robots)]
current_loads = [0] * num_robots

# Simple heuristic: assign cities to the nearest available robot that has enough remaining capacity
for city in range(1, len(coordinates)):  # Start at 1 to skip the depot
    min_dist = float('inf')
    best_robot = None
    for robot in range(num_robots):
        if current_loads[robot] + demands[city] <= capacity:
            dist = distance(0, city)
            if dist < min_dist:
                min_dist = dist
                best_robot = robot
    if best_robot is not None:
        tours[best_robot].append(city)
        current_loads[best_robot] += demands[city]

# Each tour must start and end at the depot
for tour in tours:
    tour.insert(0, 0)
    tour.append(0)

# Calculate travel costs for each tour
total_costs = []
for tour in tours:
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += distance(tour[i], tour[i+1])
    total_costs.append(tour_json)

# Output results
overall_cost = sum(total_costs)
for robot_id, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")