import math
from itertools import permutations
from heapq import heappop, heappush

# Coordinate and demand data:
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Number of robots and their capacity:
num_robots = 8
robot_capacity = 40

# Calculate Euclidean Distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distances matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initialization of solution:
tours = [[] for _ in range(num_robots)]
load = [0] * num_robots
tour_costs = [0] * num_robots

# Heuristic solution: Nearest Neighbor with capacity constraints
for city in range(1, len(coordinates)):
    best_robot = None
    min_additional_cost = float('inf')
    
    for robot_id in range(num_robots):
        if tours[robot_id]:
            last_city = tours[robot_id][-1]
        else:
            last_city = 0  # start at the depot
        
        if load[robot_id] + demands[city] <= robot_capacity:
            additional_cost = distances[last_city][city] - distances[last_city][0]
            if additional_cost < min_additional_cost:
                min_additional_cost = additional_cost
                best_robot = robot_id
    
    if best_robot is not None:
        if tours[best_robot]:
            last_city = tours[best_robot][-1]
        else:
            last_city = 0  # start at the depot
        tours[best_robot].append(city)
        load[best_robot] += demands[city]
        tour_costs[best_robot] += distances[last_city][city]

# Close all tours at depot
for robot_id in range(num_robots):
    if tours[robot_id]:
        last_city = tours[robot_id][-1]
        tour_costs[robot_id] += distances[last_city][0]
        tours[robot_id].append(0)

# Print All Tours
overall_cost = 0
for robot_id in range(num_robots):
    if tours[robot_id]:
        print(f"Robot {robot_id} Tour: {[0] + tours[robot_id]}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_costs[robot_id]:.2f}")
        overall_cost += tour_costs[robot_id]

print(f"Overall Total Travel Cost: {overall_cost:.2f}")