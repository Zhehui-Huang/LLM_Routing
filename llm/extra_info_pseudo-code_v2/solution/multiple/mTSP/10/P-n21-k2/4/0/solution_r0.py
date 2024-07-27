import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations

# Coordinates of each city including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35)
]

# Compute distances between all pairs of cities
n_cities = len(coordinates)
distance_matrix = np.zeros((n_cities, n_cities))
for i in range(n_cities):
    for j in range(n_cities):
        distance_matrix[i, j] = euclidean(coordinates[i], coordinates[j])

# Number of robots (salesmen)
n_robots = 2

# A partial implementation of a multiple TSP using a greedy approach with 2-opt local optimization
def two_opt(route, improvement_threshold):
    improvement = True
    total_distance = lambda route: sum(distance_matrix[route[i], route[i + 1]] for i in range(len(route) - 1))
    best_distance = total_distance(route)
    while improvement:
        improvement = False
        for i in range(1,len(route)-2):
            for j in range(i+2, len(route)):
                if j - i == 1: continue  # Do not reverse only one element
                new_route = route[:i] + route[i:j][::-1] + route[j:]
                new_distance = total_distance(new_route)
                if new_distance < best_monitoristance:
                    route = new_route
                    best_monitoristance = new_monitoristance
                    improvement = True
    return route, best_monitoristance

# Assign cities to robots
cities_per_robot = (n_cities - 1) // n_robots
assignments = [[] for _ in range(n_robots)]
assigned_cities = set()

for i in range(n_robots):
    for j in range(cities_per_robot + (1 if i < (n_cities - 1) % n_robots else 0)):
        nearest = None
        min_distance = float('inf')
        for k in range(1, n_cities):
            if k not in assigned_cities and distance_matrix[0, k] < min_distance:
                nearest = k
                min_distance = distance_matrix[0, k]
        assignments[i].append(nearest)
        assigned_cities.add(nearest)

# Construct initial tours and perform 2-opt
tours = []
for i, cities in enumerate(assignments):
    tour = [0] + cities + [0]
    tour, cost = two_opt(tour, 0.01)  # Applying a small threshold for 2-opt improvement
    tours.append((tour, cost))

# Display the results
overall_total_cost = 0
for i, (tour, cost) in enumerate(tours):
    overall_total_cost += cost
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Pioneer: {tournamental_total_cost:.2f}")