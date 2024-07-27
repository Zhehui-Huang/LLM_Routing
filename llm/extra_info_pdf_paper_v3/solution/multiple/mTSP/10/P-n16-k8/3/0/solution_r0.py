import math
from itertools import permutations

# City Coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69)
]

# Calculate Euclidean Distance between two cities
def distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Generate distance matrix
n_cities = len(city_coords)
distance_matrix = [[distance(i, j) for j in range(n_cities)] for i in range(n_cities)]

# Number of robots
num_robots = 8

# Assign cities to robots round-robin or other simple method
cities_per_robot = [[] for _ in range(num_robots)]
for i in range(1, n_cities):  # Start from 1 to skip the depot city
    cities_per_robot[i % num_robots].append(i)

# Create function to find the shortest path for a given set of cities including the return to the depot
def find_tour(cities):
    min_path_cost = float('inf')
    min_path = None
    for perm in permutations(cities):
        # include depot at start and end
        path = [0] + list(perm) + [0]
        path_cost = sum(distance_matrix[path[i]][path[i+1]] for i in range(len(path) - 1))
        if path_cost < min_path_cost:
            min_path_cost = path_cost
            min_path = path
    return min_path, min_path_cost

# Calculate tours for each robot
overall_total_cost = 0
for i in range(num_robots):
    tour, tour_cost = find_tour(cities_per_robot[i])
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")
    overall_total_cost += tour_cost

# Output the overall total travel cost
print(f"Overall Total Travel Cost: {overall_total_cost}")