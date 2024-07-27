import math
import numpy as np
from itertools import permutations

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt(sum((city1[i] - city2[i])**2 for i in range(2)))

# Cities coordinates (index corresponds to city number)
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

# Number of robots
num_robots = 8

# Initialize robots tours as lists
robot_tours = {i: [] for i in range(num_robots)}

# Assign cities (excluding depot 0) roughly equally to each robot
visited = set()
currentIndex = 1
for i in range(num_robots):
    robot_tours[i].append(0)  # start with depot
    if i == num_robots - 1:
        # Assign remaining cities to the last robot
        remaining_cities = [c for c in cities.keys() if c not in visited and c != 0]
        robot_tours[i].extend(remaining_cities)
    else:
        # Assign a roughly equal portion of cities
        num_cities_per_robot = len(cities) // num_robots
        assignments = 0
        while assignments < num_cities_per_robot and currentIndex < len(cities):
            if currentIndex not in visited:
                robot_tours[i].append(currentIndex)
                visited.add(currentIndex)
                assignments += 1
            currentIndex += 1
    robot_tours[i].append(0)  # end with depot

# Function to apply 2-opt swap to optimize tour
def two_opt(route):
    best = route
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1: continue
                new_route = route[:]
                new_route[i:j] = route[j-1:i-1:-1]
                if sum(euclidean_distance(cities[new_route[k]], cities[new_route[k+1]]) for k in range(len(new_route) - 1)) < sum(euclidean_distance(cities[best[k]], cities[best[k+1]]) for k in range(len(best) - 1)):
                    best = new_route
                    improved = True
        route = best
    return best

# Optimize each robot's tour using 2-opt
optimized_tours = {}
total_cost = 0
for r in robot_tours:
    optimized_tours[r] = two_opt(robot_tours[r])
    tour_cost = sum(euclidean_distance(cities[optimized_tours[r][i]], cities[optimized_tours[r][i+1]]) for i in range(len(optimized_tours[r]) - 1))
    total_cost += tour_cost
    print(f"Robot {r} Tour: {optimized_tours[r]}")
    print(f"Robot {r} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")