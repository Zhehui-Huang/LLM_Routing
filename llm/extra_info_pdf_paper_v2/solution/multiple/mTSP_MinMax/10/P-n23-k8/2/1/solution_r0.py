import math
import random
from itertools import permutations

# City coordinates
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

# Distance calculation using Euclidean distance
def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of robots
num_robots = 8

# Initial greedy assignment based on nearest neighbor
def initial_solution_greedy():
    tour_list = [[] for _ in range(num_robots)]
    city_list = list(cities.keys())[1:]  # exclude the depot city
    random.shuffle(city_list)
    current_position = [0] * num_robots
    min_tour_lengths = [0] * num_robots

    while city_list:
        for r in range(num_robots):
            if not city_list:
                break
            # Find nearest unvisited city
            nearest_city = min(city_list, key=lambda c: calculate_distance(current_position[r], c))
            distance_to_city = calculate_distance(current_position[r], nearest_city)
            tour_list[r].append(nearest_city)
            min_tour_lengths[r] += distance_to_city
            current_position[r] = nearest_city
            city_list.remove(nearest_city)

        # Return to depot
    for r in range(num_robots):
        if tour_list[r]:  # if the robot has visited any city
            min_tour_lengths[r] += calculate_distance(tour_list[r][-1], 0)
            tour_list[r].insert(0, 0)
            tour_list[r].append(0)

    return tour_list, min_tour_lengths

# Calculate total tour cost
def tour_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += calculate_distance(tour[i], tour[i+1])
    return cost

# Solution initialization
solution, costs = initial_solution_greedy()
max_cost = max(costs)

# Displaying results
for idx, tour in enumerate(solution):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {costs[idx]}")

print("\nMaximum Travel Cost:", max_cost)