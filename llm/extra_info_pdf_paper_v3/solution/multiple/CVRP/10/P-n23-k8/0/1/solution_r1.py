import math
import random

# City positions and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 
    8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 
    15, 5, 10
]

# Parameters
num_robots = 8
robot_capacity = 40
depot = 0

def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def nearest_neighbor(current_city, remaining_cities, load, capacity):
    min_distance = float('inf')
    next_city = None
    for city in remaining_cities:
        if demands[city] <= (capacity - load):
            distance = euclidean_distance(current_city, city)
            if distance < min_distance:
                min_distance = distance
                next_city = city
    return next_city

def solve_cvrp():
    tours = [[] for _ in range(num_robots)]
    total_costs = [0 for _ in range(num_robots)]
    remaining_cities = set(range(1, len(coordinates))) # exclude the depot city
    robot_loads = [0] * num_robots

    # Assign tours to robots
    for robot in range(num_robots):
        current_city = depot
        tours[robot].append(current_city)
        while remaining_cities and robot_loads[robot] < robot_capacity:
            next_city = nearest_neighbor(current_city, remaining_cities, robot_loads[robot], robot_capacity)
            if next_city is None:
                break
            tours[robot].append(next_city)
            remaining_cities.remove(next_city)
            total_costs[robot] += euclidean_distance(current_city, next_city)
            robot_loads[robot] += demands[next_city]
            current_city = next_city

        # Return to depot
        if tours[robot][-1] != depot:
            tours[robot].append(depot)
            total_costs[robot] += euclidean_distance(current_city, depot)

    overall_cost = sum(total_costs)
    return tours, total_costs, overall_cost

tours, total_costs, overall_cost = solve_cvrp()

# Display the results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {total_costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")