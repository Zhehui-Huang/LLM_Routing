import math
import numpy as np
import random

# City coordinates with city index as key
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
    22: (56, 37),
}

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two cities """
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Distance matrix
num_cities = len(cities)
distance_matrix = [[calculate_distance(i, j) for j in range(num_cities)] for i in range(num_cities)]

# Number of robots
num_robots = 8

def initial_solution():
    """ Simple greedy solution for initial setup, not optimized """
    non_depot_cities = list(range(1, num_cities))
    random.shuffle(non_depot_cities)
    chunks = [non_depalpot_cities[i::num_robots] for i in range(num_robots)]
    return chunks

def calculate_tour_cost(tour):
    """ Calculate the round trip cost for a single robot's tour """
    cost = 0
    current_city = 0
    for city in tour:
        cost += distance_matrix[current_city][city]
        current_city = city
    cost += distance_matrix[current_city][0]  # Return to depot
    return cost

def gvns_solution(tours):
    """ Implement the General Variable Neighborhood Search heuristic """
    # This is a skeleton placeholder for the complete heuristic
    return tours  # Should implement the actual VNS modifications

# Forming initial robot tours
tours = initial_solution()
optimized_tours = gvns_solution(tours)

# Calculating tour costs and finding the maximum
tour_costs = []
for tour in optimized_tours:
    tour_with_depot = [0] + tour + [0]
    cost = calculate_tour_cost(tour_with_depot)
    tour_costs.append(cost)
    print(f"Robot Tour: {tour_with_depot}")
    print(f"Robot Total Travel Cost: {cost}")

max_cost = max(tour_costs)
print(f"Maximum Travel Cost: {max_cost}")