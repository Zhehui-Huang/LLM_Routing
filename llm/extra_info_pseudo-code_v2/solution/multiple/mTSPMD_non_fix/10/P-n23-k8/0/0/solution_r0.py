import numpy as np
import random
from math import sqrt

# Global setup based on the problem statement 
cities = {
    i: coord for i, coord in enumerate([
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
        (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
        (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
    ])
}
num_cities = len(cities)
depots = list(range(6))  # Considering depots up to index 5
robots = 8  # Number of robots as per the problem
start_depot = 0  # All robots start from the same depot

# Objective 1: Calculate the Euclidean distance between two cities
def calc_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Objective 2: Generate the initial population for the Genetic Algorithm
def generate_initial_population(pop_size, num_cities, num_robots):
    population = []
    for _ in range(pop_size):
        # Create a sequence of cities with depots as separators for robots
        city_list = list(range(num_cities))
        random.shuffle(city_list)
        depot_indices = sorted(random.sample(range(1, num_cities - 1), num_robots - 1))
        individual = []
        last_index = 0
        for index in depot_indices:
            individual.extend(city_list[last_index:index])
            individual.append(-1)
            last_index = index
        individual.extend(city_list[last_index:])
        population.append(individual)
    return population

# Example usage:
pop_size = 50  # Size of the population
initial_population = generate_initial_population(pop_size, num_cities, robots)

# Continued steps:
# - Parent Selection
# - Mutation and Crossover
# - Fitness Evaluation
# - Main Genetic Algorithm Execution Loop