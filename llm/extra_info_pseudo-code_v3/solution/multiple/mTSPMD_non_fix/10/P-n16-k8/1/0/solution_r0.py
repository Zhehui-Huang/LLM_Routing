import numpy as np
from scipy.spatial.distance import euclidean
import random

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

num_robots = 8
num_cities = len(cities)

# Function to calculate distance matrix
def calculate_distance_matrix(cities):
    num_cities = len(cities)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                dist_matrix[i, j] = euclidean(cities[i], cities[j])
            else:
                dist_matrix[i, j] = float('inf')  # no loops
    return dist_matrix

distance_matrix = calculate_distance_matrix(cities)

# Heuristic: Nearest Neighbor Search for initial solution
def nearest_neighbor(num_robots, num_cities, distance_matrix):
    tours = [[] for _ in range(num_robots)]
    free_cities = set(range(1, num_cities))  # Exclude the depot 0 initially
    used_cities = set()

    # Initial step: allocate each robot a nearest city from the depot
    for r in range(num_robots):
        nearest = min(free_cities, key=lambda x: distance_matrix[0][x])
        tours[r].append(0)
        tours[r].append(nearest)
        used_cities.add(nearest)
        free_cities.remove(nearest)

    # Allocate remaining cities
    while free_cities:
        for tour in tours:
            if free_cities:
                last_city = tour[-1]
                nearest = min(free_cities, key=lambda x: distance_matrix[last_city][x])
                tour.append(nearest)
                used_cities.add(nearest)
                free_cities.remove(nearest)

    # Complete each tour by returning to the depot
    for tour in tours:
        tour.append(0)  # back to depot

    return tours

# Calculate tour costs
def calculate_tour_cost(tour, distance_matrix):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance_matrix[tour[i]][tour[i + 1]]
    return cost

# Initialize robots' tours
tours = nearest_neighbor(num_robots, num_cities, distance_matrix)
tour_costs = [calculate_tour_cost(tour, distance_matrix) for tour in tours]
total_cost = sum(tour_costs)

# Output results
for idx, tour in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_costs[idx]}")

print(f"Overall Total Travel Cost: {total_cost}")