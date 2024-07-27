import math
import random

# City coordinates (ID and Cartesian coordinates)
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35),
    21: (32, 39),
    22: (56, 37)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Compute cost of a route
def cost(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

# Generate initial tours for robots by distributing cities evenly
def initial_tours(n_robots, n_cities):
    tours = {i: [0] for i in range(n_robots)}
    for city in range(1, n_cities):
        tours[city % n_robots].append(city)
    for tour in tours.values():
        tour.append(0)  # Return to depot
    return tours

# 2-Opt optimization for single tour
def two_opt(tour):
    best = tour
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 2, len(tour)):
                new_route = tour[:]
                new_route[i:j] = reversed(tour[i:j])
                if cost(new_route) < cost(best):
                    best = new_route
                    improved = True
    return best

# Initialize tours and optimize using 2-opt
initial_t = initial_tours(8, len(cities))
optimized_tours = {robot: two_opt(tour) for robot, tour in initial_t.items()}

# Output results
total_cost = 0
for robot, tour in optimized_tours.items():
    tour_cost = cost(tour)
    total_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")