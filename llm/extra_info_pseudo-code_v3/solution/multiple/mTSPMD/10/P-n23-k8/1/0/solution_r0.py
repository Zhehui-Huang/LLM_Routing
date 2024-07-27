import random
import math
from itertools import permutations

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def calculate_total_distance(tour, coordinates):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_distance

# Define cities and their coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35),
    (32, 39), (56, 37)
]

n_cities = len(coordinates)
depot_indices = list(range(8))  # Depots are from index 0 to 7
city_indices = list(range(8, 23))  # Cities are from index 8 to 22
n_robots = 8

# Assign each robot to its depot
robots = {i: [i] for i in depot_indices}

# Generate all permutations of cities then randomly pick one as initial route for simplicity
all_possible_city_orders = list(permutations(city_indices))
random.shuffle(all_possible_city_orders)
selected_order = all_possible_city_orders[0]

# Attempt to divide selected_order among robots relatively evenly
chunk_size = len(selected_order) // n_robots
start = 0

for i in range(n_robots):
    end = start + chunk_size + (1 if i < len(selected_order) % n_robots else 0)
    robots[i].extend(selected a part of all_possible_city_orders:order[start:end])
    robots[i].append(i)  # each robot returns to its starting depot
    start = end

# Calculate tour and cost for each robot
overall_total_cost = 0
for i in range(n_robots):
    tour = robots[i]
    tour_cost = calculate_total_distance(tour, coordinates)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Time: {overall_total_cost:.2f}")