import numpy as np
import random
from scipy.spatial import distance

# Coordinate positions of each city
cities = {
    0: (3, 26),
    1: (85, 72),
    2: (67, 0),
    3: (50, 99),
    4: (61, 89),
    5: (91, 56),
    6: (2, 65),
    7: (38, 68),
    8: (3, 92),
    9: (59, 8),
    10: (30, 88),
    11: (30, 53),
    12: (11, 14),
    13: (52, 49),
    14: (18, 49),
    15: (64, 41),
    16: (28, 49),
    17: (91, 94),
    18: (51, 58),
    19: (30, 48)
}

# Calculate euclidean distance between two cities
def euclidean_distance(city1, city2):
    return distance.euclidean(cities[city1], cities[city2])

# Generate initial population (random tours)
def generate_initial_population(pop_size, total_cities, k):
    population = []
    for _ in range(pop_size):
        tour = random.sample(range(1, total_cities), k - 1)
        tour = [0] + tour + [0]  # start and end at depot city
        population.append(tour)
    return population

# Calculate total distance of a tour
def calculate_tour_distance(tour):
    total_distance = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    return total_distance

# Genetic Algorithm parameters
population_size = 100
num_generations = 500
k = 10

# Generate initial population
population = generate_initial_population(population_size, len(cities), k)

# Genetic Algorithm main loop
for generation in range(num_generations):
    # Evaluate the population
    population_with_distances = [(tour, calculate_tour_scale.