import numpy as as np
from itertools import permutations
from math import sqrt

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Generate a distance matrix from city coordinates
def generate_distance_matrix(cities):
    n = len(cities)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean_distance(cities[i], cities[j])
    return distance_matrix

# Find the nearest neighbor tour starting from each robot's assigned start city
def find_tours(n_robots, cities, distance_matrix):
    visited = set()
    tours = [[] for _ in range(n_robots)]
    remaining_cities = set(range(1, len(cities)))  # Exclude the depot city 0

    # Assign initial cities nearly equidistant from the depot for each robot
    for i in range(n_robots):
        if remaining_cities:
            next_city = min(remaining_cities, key=lambda x: distance_matrix[0][x])
            remaining_cities.remove(next_city)
            tours[i].append(0)
            tours[i].append(next_city)
            visited.add(next_city)

    # Continue finding nearest neighbors for each robot's last city until all cities are visited
    while remaining_cities:
        for i in range(n_robots):
            if remaining_cities:
                last_city = tours[i][-1]
                next_city = min(remaining_cities, key=lambda x: distance_matrix[last_city][x])
                tours[i].append(next_city)
                remaining_cities.remove(next_city)
                visited.add(next_city)

    # Close each tour by returning to the depot
    for tour in tours:
        if tour[-1] != 0:
            tour.append(0)

    return tours

# Calculate the cost of each tour
def calculate_total_cost(tours, distance_matrix):
    total_cost = 0
    results = []
    for idx, tour in enumerate(tours):
        tour_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
        results.append((tour, tour_cost))
        total_cost += tour_cost
    return results, total_cost

# City coordinates initialization
cities = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
          (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
          (58, 27), (37, 69)]

# Configuration for robots
n_robots = 8

# Generate distance matrix
distance_matrix = generate_distance_matrix(cities)

# Determine tours using nearest neighbors from initial spread
tours = find_tours(n_robots, cities, distance_matrix)

# Calculate and print tour costs
results, overall_total_cost = calculate_total_cost(tours, distance_matrix)
for i, (tour, cost) in enumerate(results):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")