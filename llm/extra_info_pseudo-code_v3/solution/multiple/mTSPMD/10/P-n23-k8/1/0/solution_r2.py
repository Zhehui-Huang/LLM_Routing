import random
import math

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

# Robot starting depots (from 0 to 7)
depot_indices = list(range(8))
city_indices = list(range(8, 23)) # Cities are from index 8 to 22
random.shuffle(city_indices)  # Shuffle city indices for random initial solution

# Assign cities to robots
robots = {i: [i] for i in depot_indices}
chunk_size = len(city_indices) // len(depot_indices)
extras = len(city_indices) % len(depot_indices)

start = 0
for i in range(len(depot_indices)):
    end = start + chunk_size + (1 if i < extras else 0)
    robots[depot_indices[i]].extend(city_indices[start:end])
    robots[depot_indices[i]].append(depot_indices[i])  # End at their respective depot
    start = end

# Calculate tour and cost for each robot
overall_total_cost = 0
for i in range(len(depot_indices)):
    tour = robots[depot_indices[i]]
    tour_cost = calculate_total_distance(tour, coordinates)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")