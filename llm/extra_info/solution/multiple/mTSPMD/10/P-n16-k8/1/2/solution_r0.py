import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# City coordinates where indices represent city ids
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Number of robots, respective depot cities and ID assignment
num_robots = 8
robot_depots = {i: i for i in range(num_robots)}  # Depot cities are 0 to 7

# Calculate distances matrix
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distance_matrix[i, j] = euclidean(cities[i], cities[j])

# Assign cities to robots based on nearest depot heuristic
assignments = {i: [i] for i in range(num_robots)}  # each robot starts with its depot city
for city_id in range(num_robots, num_cities):
    nearest_depot = min([(euclidean(cities[city_id], cities[depot]), depot)
                         for depot in robot_depots.values()], key=lambda x: x[0])[1]
    assignments[nearest_depot].append(city_id)

# Function to calculate the cost of a given path
def path_cost(path):
    return sum(distance_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))

# 2-opt Algorithm for route improvement
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue  # skip consecutive nodes as no change occurs
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                if path_cost(new_route) < path_cost(best):
                    best = new_route
                    improved = True
        route = best
    return best

optimized_routes = {}
total_cost = 0

for robot_id, cities_list in assignments.items():
    cities_list.append(robot_depots[robot_id])  # append depot to end to complete tour
    if len(cities_list) > 2:
        optimized_route = two_opt(cities_list)
    else:
        optimized_route = cities_list
    route_cost = path_cost(optimized_route)
    optimized_routes[robot_id] = (optimized_route, route_cost)
    total_cost += route_cost
    print(f"Robot {robot_id} Tour: {optimized_route}")
    print(f"Robot {robot_id} Total Travel Cost: {route_cost}")

print(f"Overall Total Travel Cost: {total_cost}")