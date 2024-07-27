import numpy as np
from scipy.spatial.distance import euclidean

# Coordinates of each city including depot city at index 0
cities_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 34), (62, 63), (63, 69), (45, 35)
]

# Calculate distance matrix
def calculate_distance_matrix(cities):
    n = len(cities)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] = euclidean(cities[i], cities[j])
    return matrix

distance_matrix = calculate_distance_matrix(cities_coordinates)

# Number of robots
num_robots = 2

# Split cities among robots heuristically (a simple heuristic to evenly distribute cities to open up further solution improvement)
def divide_cities(city_count, num_robots):
    cities_per_robot = city_count // num_robots
    remainder = city_count % num_robots
    boundaries = []
    start = 1
    for i in range(num_robots):
        end = start + cities_per_robot
        if remainder > 0:
            end += 1
            remainder -= 1
        boundaries.append(list(range(start, end)))
        start = end
    return boundaries

city_boundaries = divide_cities(len(cities_coordinates) - 1, num_robots)

# Function to compute tour cost and path
def compute_tour_cost(cities):
    total_cost = 0
    path = [0]  # Start at the depot
    current = 0
    for city in cities:
        total_cost += distance_matrix[current][city]
        path.append(city)
        current = city
    total_cost += distance_matrix[current][0]  # Return to depot
    path.append(0)  # End at depot
    return total_cost, path

# Collect tours and compute the cost for each tour
tours = []
max_cost = 0
for robot in range(num_robots):
    cost, path = compute_tour_cost(city_boundaries[robot])
    tours.append((path, cost))
    max_cost = max(max_cost, cost)

# Output the results as specified
for i, (path, cost) in enumerate(tours):
    print(f"Robot {i} Tour: {path}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_cost}")