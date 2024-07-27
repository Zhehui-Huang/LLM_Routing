import numpy as np
import math

# Define cities and their coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of robots
num_robots = 4

# Calculate the Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Build distance matrix
num_cities = len(cities)
dist_matrix = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        dist_matrix[i][j] = calc_distance(i, j)

# Assign cities to robots using a simple heuristic: nearest neighbour
tours = [[] for _ in range(num_robots)]
visited = set()

# All robots start from depot city 0
current_positions = [0] * num_robots
for r in range(num_robots):
    tours[r].append(0)
    visited.add(0)

# Allocation of cities to robots
for _ in range(1, num_cities):
    for r in range(num_robots):
        # Find nearest non-visited city
        current_city = current_positions[r]
        next_city = None
        min_distance = float('inf')
        for city in range(num_cities):
            if city not in visited and dist_matrix[current_city][city] < min_distance:
                min_distance = dist_matrix[current_city][city]
                next_city = city
        if next_city is not None:
            tours[r].append(next_city)
            visited.add(next_city)
            current_positions[r] = next_city

# Calculate costs for each tour
total_costs = []
overall_cost = 0
for r in range(num_robots):
    tour_cost = sum(dist_matrix[tours[r][i]][tours[r][i + 1]] for i in range(len(tours[r]) - 1))
    total_costs.append(tour_cost)
    overall_cost += tour_cost
    print(f"Robot {r} Tour: {tours[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")