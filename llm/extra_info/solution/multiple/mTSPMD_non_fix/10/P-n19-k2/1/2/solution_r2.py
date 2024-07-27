import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of all cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Distance matrix calculation
def create_distance_matrix(cities):
    keys = list(cities.keys())
    size = len(keys)
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i != j:
                matrix[i][j] = euclidean(cities[keys[i]], cities[keys[j]])
            else:
                matrix[i][j] = float('inf')
    return matrix

dist_matrix = create_distance_matrix(cities)

# Nearest neighbor heuristic function
def nearest_neighbor(num_robots, start_depot, cities, dist_matrix):
    unvisited = set(cities.keys())
    tours = [[] for _ in range(num_robots)]
    costs = [0 for _ in range(num_robots)]
    current_pos = [start_depot for _ in range(num_robots)]

    while unvisited:
        for r in range(num_robots):
            if len(unvisited) == 0:
                break
            next_city = min(unvisited, key=lambda x: dist_matrix[current_pos[r], x])
            tours[r].append(next_city)
            costs[r] += dist_matrix[current_pos[r], next_city]
            current_pos[r] = next_city
            unvisited.remove(next_city)

    return tours, costs

# Assign robots to start from depot 0 and solve the TSP
robot_start = 0  # depot 0
num_robots = 2  # total robots
all_cities = cities.keys()

tours, costs = nearest_neighbor(num_robots, robot_start, cities, dist_matrix)
overall_cost = sum(costs)

# Append start depot to each tour for output format
for tour in tours:
    tour.insert(0, robot_start)  # prepend the starting depot

# Output results
for i in range(num_robots):
    print(f"Robot {i} Tour: {tours[i]}")
    print(f"Robot {i} Total Travel Cost: {costs[i]}")

print(f"Overall Total Travel Cost: {overall_cost}")