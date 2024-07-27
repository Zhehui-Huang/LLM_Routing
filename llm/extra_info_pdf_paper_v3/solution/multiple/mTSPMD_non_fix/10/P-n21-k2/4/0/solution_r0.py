import math
import random

# Define the cities and their coordinates
cities = {
    0: (30, 40), # depot 0
    1: (37, 52), # depot 1
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
    20: (45, 35)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Initialize robots
robots = {0: [0], 1: [1]}  # Depot allocations

# Cities that need distributing
other_cities = list(set(cities.keys()) - {0, 1})

# Greedy nearest-neighbor to assign cities to nearest depot initially
for city in other_cities:
    nearest_depot = min([0, 1], key=lambda d: distance(d, city))
    robots[nearest_depot].append(city)

def total_tour_cost(tour):
    return sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1)) + distance(tour[-1], tour[0])

# Attempting to optimize each tour using simple two-opt swap
def two_opt(tour):
    min_change = True
    while min_change:
        min_change = False
        best_distance = total_tour_cost(tour)
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour)):
                if j - i == 1: continue
                new_tour = tour[:i] + tour[i:j][::-1] + tour[j:]
                new_distance = total_tour_cost(new_tour)
                if new_distance < best_distance:
                    tour = new_tour
                    best_distance = new_distance
                    min_change = True
        return tour

# Refine tours with two_opt
for key in robots:
    robots[key] = two_opt(robots[key] + [robots[key][0]])  # Making them round trips initially for simplicity

# Compute costs
robot_costs = {key: total_tour_cost(robots[key]) for key in robots}
overall_cost = sum(robot_costs.values())

# Output tours and costs
for key in robots:
    print(f"Robot {key} Tour: {robots[key]}")
    print(f"Robot {key} Total Travel Cost: {robot_costs[key]}")
print(f"Overall Total Travel Cost: {overall_cost}")