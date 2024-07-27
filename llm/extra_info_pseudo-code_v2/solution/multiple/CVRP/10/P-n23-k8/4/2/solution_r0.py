import numpy as np

# City coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14,
           6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Calculate the Euclidean distance matrix
def calculate_distances(coords):
    n = len(coords)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist_matrix[i, j] = np.linalg.norm(np.array(coords[i]) - np.array(coords[j]))
    return dist_matrix

distance_matrix = calculate_distances(coordinates)

# Number of robots and their capacities
robot_count = 8
robot_capacity = 40

# CRWP Initialization
def initialize_savings(distance_matrix):
    n = len(distance_matrix)
    savings = []
    for i in range(1, n):  # Start from 1 to skip the depot
        for j in range(i + 1, n):
            if i != j:
                savings.append((i, j, distance_matrix[0, i] + distance_block[0, j] - distance_matrix[i, j]))
    return sorted(savings, key=lambda x: x[2], reverse=True)

savings = initialize_savings(distance_matrix)

# Assign routes to robots
routes = [[] for _ in range(robot_count)]
remaining_demand = list(demands)
capacity_remaining = [robot_capacity] * robot_count
current_location = [0] * robot_count

while any(remaining_demand[1:]):  # While there's any demand excluding depot
    for robot_id in range(robot_count):
        if remaining_demand[current_location[robot_id]] == 0:
            best_next_city = None
            max_saving = float('-inf')
            for city_id, city_demand in enumerate(remaining_demand):
                if city_demand > 0 and capacity_remaining[robot_id] >= city_demand:
                    possible_saving = savings[(current_location[robot_id], city_id)]
                    if possible_saving > max_saving:
                        max_saving = possible_saving
                        best_next_city = city_id
            if best_next_city:
                routes[robot_id].append(best_next_city)
                remaining_demand[best_next_city] = 0
                capacity_remaining[robot_id] -= demands[best_next_city]
                current_location[robot_id] = best_next_city

# Add return to depot
for route in routes:
    route.append(0)

# Print the solution
overall_cost = 0
for robot_id, route in enumerate(routes):
    total_cost = sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1))
    overall_cost += total_cost
    print(f"Robot {robot_id} Tour: {route}")
    print(f"Robot {robot_id} Total Travel Cost: {total_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")