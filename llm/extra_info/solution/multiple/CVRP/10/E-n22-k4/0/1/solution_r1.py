import numpy as n
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
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Setup the output storage for each robot's tour and cost
robot_tours = [[] for _ in range(num_robots)]
remaining_capacity = [capacity] * num_robots

# Assign cities to robots in a simple heuristic manner - based on the order and capacity
for city in range(1, len(coordinates)):  # start at 1 to skip the depot
    assigned = False
    for robot in range(num_robots):
        if remaining_capacity[robot] >= demands[city]:
            robot_tours[robot].append(city)
            remaining_capacity[robot] -= demands[city]
            assigned = True
            break
    if not assigned:
        print("Error: Not enough capacity to assign city", city)

# Calculate tour details
total_overall_cost = 0
for i in range(num_robots):
    tour = [0] + robot_tours[i] + [0]  # start and end at depot
    tour_cost = 0
    for j in range(len(tour) - 1):
        tour_cost += distance(tour[j], tour[j+1])
    
    total_overall_cost += tour_cost
    
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_overall_cost:.2f}")