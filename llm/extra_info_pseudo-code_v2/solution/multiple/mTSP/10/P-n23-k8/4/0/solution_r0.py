import numpy as np
from math import sqrt

def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def initialize_distances(cities):
    num_cities = len(cities)
    distances = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            distances[i][j] = euclidean_distance(cities[i], cities[j])
    return distances

# Initialize cities
cities = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Initialize number of robots
num_robots = 8

# Calculate distances between cities
distances = initialize_distances(cities)

# Assignment to robots using a simple round-robin approach
assignments = {i: [] for i in range(num_robots)}
for city_index in range(1, len(cities)):  # Start from 1 to exclude depot
    assignments[city_index % num_robots].append(city_index)

def nearest_neighbor_tour(start, cities, remaining_cities):
    tour = [start]
    current = start
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda x: distances[current][x])
        tour.append(next_city)
        current = next_city
        remaining_cities.remove(next_city)
    tour.append(start)  # return to the depot
    return tour

def calculate_total_cost(tour, distances):
    return sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Create initial tours for each robot using nearest neighbor heuristic
tours = {}
total_costs = {}
overall_total_cost = 0

for robot in range(num_robots):
    if not assignments[robot]:
        continue
    tour = nearest_neighbor_tour(0, cities, assignments[robot])
    tours[robot] = tour
    cost = calculate_total_cost(tour, distances)
    total_costs[robot] = cost
    overall_total_cost += cost

# Output results
for robot in range(num_robots):
    if robot in tours:
        print(f"Robot {robot} Tour: {tours[robot]}")
        print(f"Robot {robot} Total Travel Cost: {total_costs[robot]:.2f}")

print(f"Overall Total Travel Cost: {overall_total_cost:.2f}")