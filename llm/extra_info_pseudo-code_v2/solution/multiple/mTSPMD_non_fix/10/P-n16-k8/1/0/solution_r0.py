import numpy as np
import random
from math import sqrt

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

# Number of robots and their starting location
num_robots = 8
start_depot = 0

# Euclidean distance calculator
def euclidean_distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Generate initial feasible solution
def generate_initial_solution(num_cities, num_robots):
    city_list = list(range(1, num_cities))  # start from 1 since 0 is depot
    random.shuffle(city_list)
    parts = []
    approx_part_length = len(city_list) // num_robots
    for i in range(num_robots - 1):
        parts.append(city_list[i * approx_part_length:(i + 1) * approx_part_length])
    parts.append(city_list[(num_robots - 1) * approx_part_length:])  # remaining cities
    tours = [[0] + part + [0] for part in parts]  # Adding depot at the start and end of each tour
    return tours

# Calculate total travel cost for a tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Initial solution
tours = generate_initial_solution(len(cities), num_robots)

# Calculate costs
tour_costs = [calculate_tour_cost(tour) for tour in tours]
overall_cost = sum(tour_costs)

# Display solution
for i, (tour, cost) in enumerate(zip(tours, tour_costs)):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")