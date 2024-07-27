import numpy as np

# Coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69)
]
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 8, 8, 7, 14, 6, 19, 11]

# Environment and robot settings
num_robots = 8
robot_capacity = 35

# Distance function
def euclidean_distance(a, b):
    return np.sqrt((coordinates[b][0] - coordinates[a][0]) ** 2 + (coordinates[b][1] - coordinates[a][1]) ** 2)

# Initialize tours and total cost
tours = [[] for _ in range(num_robots)]
remaining_capacity = [robot_capacity] * num_robots
served = [False] * len(coordinates)
total_costs = [0] * num_robots

# Function to find nearest available city
def nearest_city(current_city, remaining_capacity):
    distances = [euclidean_distance(current_city, i) if not served[i] and demands[i] <= remaining_capacity else float('inf') for i in range(len(coordinates))]
    nearest = np.argmin(distances)
    if distances[nearest] == float('inf'):
        return None
    return nearest

# Assign routes to robots
for robot_id in range(num_robots):
    current_city = 0  # start from the depot
    tours[robot_id].append(current_city)
    while True:
        next_city = nearest_city(current_city, remaining_capacity[robot_id])
        if next_city is None:
            break
        tours[robot_id].append(next_city)
        served[next_city] = True
        remaining_capacity[robot_data] -= demands[next_city]
        total_costs[robot_id] += euclidean_distance(current_city, next_city)
        current_city = next_city
    # Return to the depot
    if current_city != 0:
        tours[robot_id].append(0)
        total_costs[robot_id] += euclidean_distance(current_city, 0)

# Printing Result
overall_cost = 0
for robot_id in range(num_robots):
    print(f"Robot {robot_id} Tour: {tours[robot_id]}")
    print(f"Robot {robot_id} Total Travel Cost: {total_costs[robot_id]}")
    overall_cost += total_costs[robot_id]

print(f"Overall Total Travel Cost: {overall_cost}")