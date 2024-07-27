import math
from itertools import permutations

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def calculate_total_cost(route, distance_matrix):
    total_cost = 0
    for i in range(len(route) - 1):
        total_cost += distance_matrix[route[i]][route[i + 1]]
    return total_cost

# Cities and coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Number of robots and their depots
num_robots = 8
robot_depots = {i: i for i in range(num_robots)}  # robot i starts/ends at city i

# Calculate distance matrix
num_cities = len(cities)
distance_matrix = [[0] * num_cities for _ in range(num_cities)]
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = euclidean_start_end = euclidean_distance(cities[i], cities[j])

# Assign cities to robots, avoiding the depot cities
assigned_cities_per_robot = {}
remaining_cities = list(range(8, num_cities))
cities_per_robot = len(remaining_cities) // num_robots

for i in range(num_robots):
    assigned_cities = remaining_cities[i * cities_per_robot:(i + 1) * cities_per_robot]
    assigned_cities_per_robot[i] = [robot_depots[i]] + assigned_cities + [robot_depots[i]]


# Find best tour for each robot
overall_total_cost = 0
for robot_id, route_cities in assigned_cities_per_robot.items():
    best_cost = float('inf')
    best_route = None

    for route in permutations(route_cities):
        if route[0] == robot_depots[robot_id] and route[-1] == robot_depots[robot_id]:
            cost = calculate_total_cost(route, distance_matrix)
            if cost < best_cost:
                best_cost = cost
                best_route = route

    overall_total_cost += best_cost
    print(f"Robot {robot_id} Tour: {best_route}")
    print(f"Robot {robot_id} Total Travel Cost: {best_cost:.2f}")

print(f"Overall Total Travel Cost: {overall_total_tstart_end = euclidean_distance(cities[i], cities[j])cost:.2f}")