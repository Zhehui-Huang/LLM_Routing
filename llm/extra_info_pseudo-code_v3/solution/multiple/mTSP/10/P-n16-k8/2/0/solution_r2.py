import math
from itertools import cycle

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Generate distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Assign a cycle of robots to manage round-robin assignment
robot_cycle = cycle(range(num_robots))

# Greedy nearest addition in a round-robin fashion starting from the depot
tour_paths = {i: [0] for i in range(num_robots)}
available_cities = set(range(1, len(coordinates)))  # include all cities except the depot

# Assign cities to tours
while available_cities:
    for robot_id in robot_cycle:
        if not available_cities:
            break
        last_city = tour_paths[robot_id][-1]
        # Find nearest city
        nearest_city = min(available_cities, key=lambda city: distance_matrix[last_city][city])
        tour_paths[robot_id].append(nearest_city)
        available_cities.remove(nearest_city)
        
# Connecting the end of each tour back to the depot
for robot_id in tour_paths:
    tour_paths[robot_id].append(0)

# Calculate and display travel costs
total_overall_cost = 0
for robot_id in tour_paths:
    tour = tour_paths[robot_id]
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_overall_cost += tour_cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_overall_cost}")