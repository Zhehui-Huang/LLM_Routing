import math
from itertools import permutations

# Constants and input data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
               (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

num_robots = 8
vehicle_capacity = 40

# Functions
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Initial naive solution: assign cities to robots respecting capacity constraints
def initial_solution(capacity, demands, coordinates):
    routes = [[] for _ in range(num_robots)]
    current_capacities = [0] * num_robots
    robot_index = 0

    for i in range(1, len(demands)):  # start from 1, city 0 isn't visited (it's the depot)
        if current_capacities[robot_index] + demands[i] <= capacity:
            routes[robot_index].append(i)
            current_capacities[robot_index] += demands[i]
        else:
            robot_index += 1
            routes[robot_index].append(i)
            current_capacities[robot_index] += demands[i]

            if robot_index >= num_robots - 1:
                robot_index = 0  # start reassigning to the first robot if max exceed

    # Ensure all routes start and end at the depot city 0
    for route in routes:
        route.insert(0, 0)
        route.append(0)

    return routes

# Calculate distance for tours
def calculate_total_distance(tour):
    distance = 0
    for i in range(len(tour)-1):
        distance += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return distance

# Implement the initial solution
tours = initial_solution(vehicle_capacity, demands, coordinates)

# Calculate total travel cost
total_costs = [calculate_total_distance(tour) for tour in tours]
overall_cost = sum(total_costs)

# Output results
for idx, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")