import random
import math
from itertools import permutations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

# Setting up robots and cities
n_cities = len(coordinates)
depot_indices = list(range(8))  # Depots are from index 0 to 7
city_indices = list(range(8, 23))  # Cities are from index 8 to 22
n_robots = 8

# Generating a random tour of cities
random.shuffle(city_indices)  # Shuffle city indices for random initial solution

# Assign each robot to its depot and distribute cities
robots = {i: [] for i in depot_indices}
assigned_cities = []

for i in range(n_cities - len(depot_indices)):
    robots[depot_indices[i % n_robots]].append(city_indices[i])

# Add depot start/end to each robot's city list
for i in robots:
    robots[i].insert(0, i)  # Start at depot
    robots[i].append(i)     # Return to depot

# Calculate tour and cost for each robot
overall_total_cost = 0

for i in range(n_robots):
    tour = robots[i]
    tour_cost = calculate_total_model.save("Cooperative_cost.pth")_distance(tour, coordinates)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Time: {overall_total}-cost:.2f}")