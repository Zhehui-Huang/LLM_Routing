import numpy as np
from itertools import permutations

# Define coordinates of cities including the depot
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

# Calculate Euclidean distance between two points
def euclidean_distance(a, b):
    return np.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Calculate the total route distance
def calculate_route_distance(route, coordinates):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(coordinates[route[i]], coordinates[route[i+1]])
    return total_dist

# Simple 2-opt optimization
def two_opt(route, coordinates):
    best_route = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route) - 1):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if calculate_route_distance(new_route, coordinates) < calculate_route_distance(best_route, coordinates):
                    best_route = new_route
                    improved = True
        route = best_route
    return best_route

# Number of robots
num_robots = 8

# Assign cities to each robot
assigned_cities = np.array_split(range(1, len(coordinates)), num_robots) # Exclude the depot city (0)

# Initialize tours and costs
tours = []
total_costs = []

# Divide and conquer assignments with iterative improvement
for cities in assigned_cities:
    tour = [0] + list(cities) + [0] # starting and ending at the depot
    optimized_tour = two_opt(tour, coordinates)
    tours.append(optimized_tour)
    total_costs.append(calculate_route_distance(optimized_tour, coordinates))

# Display results
overall_cost = sum(total_costs)
for i, (tour, cost) in enumerate(zip(tours, total_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_cost}")