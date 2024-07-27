import math
from itertools import cycle

# Define city coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]

# Number of robots
num_robots = 8

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create distance matrix
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Initialize tours for each robot
tours = {i: [0] for i in range(num_robots)}
available_cities = set(range(1, len(coordinates)))  # city indices, excluding the depot

robot_cycle = cycle(range(num_robots))

# Greedy assignment of cities to each robot
while available_cities:
    for robot_id in robot_cycle:
        if not available_cities:
            break
        current_city = tours[robot_id][-1]
        # Find the nearest available city
        next_city = min(available_cities, key=lambda x: distance_matrix[current_city][x])
        tours[robot_id].append(next_city)
        available_cities.remove(next_city)

# Close each tour by returning to the depot city
for robot_id, tour in tours.items():
    tour.append(0)

# Compute travel costs for each robot and overall cost
total_costs = []
overall_total_cost = 0

for robot_id, tour in tours.items():
    cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_costs.append(cost)
    overall_total_cost += cost
    print(f"Robot {robot.*_} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")