import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Data given about the cities and the depot
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

num_robots = 4
depot_city = 0

# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return euclidean(cities[city1], cities[city2])

# Generate the matrix of distances between all cities
num_cities = len(cities)
distance_matrix = np.zeros((num_cities, num_cities))

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance_matrix[i][j] = calculate_distance(i, j)

# Function that evaluates the total distance of a given path
def path_distance(path):
    return sum(distance_matrix[path[i], path[i+1]] for i in range(len(path)-1))

# Implement a basic solution with a heuristic of assigning an approximately equal number of cities to each robot
cities_per_robot = (num_cities - 1) // num_robots
assignments = [[] for _ in range(num_robots)]
for index, city in enumerate(range(1, num_cities)):  # Exclude the depot for assignment
    robot_index = index // cities_per_robot
    if robot_index < num_robots:
        assignments[robot_index].append(city)

# Each robot starts at the depot, visits its assigned cities, and returns to the depot
robot_tours = [[depot_city] + assignment + [depot_city] for assignment in assignments]

# Solve a miniature TSP for each robot's tour using permutations (Not optimal for larger sizes but feasible here)
def solve_mini_tsp(tour):
    cities = tour[1:-1]  # Excludes the depot at the start and end
    best_route = None
    best_distance = float('inf')
    for perm in permutations(cities):
        current_distance = path_distance([depot_city] + list(perm) + [depot_city])
        if current_distance < best_distance:
            best_distance = current_distance
            best_route = [depot_city] + list(perm) + [depot_city]
    return best_route, best_distance

# Calculating the optimal route for each robot
overall_cost = 0
for i in range(num_robots):
    route, route_cost = solve_mini_tsp(robot_tours[i])
    robot_tours[i] = route
    print(f"Robot {i} Tour: {route}")
    print(f"Robot {i} Total Travel Cost: {route_cost}")
    overall_cost += route_cost

print(f"Overall Total Travel Challenge Cost: {overall_cost}")