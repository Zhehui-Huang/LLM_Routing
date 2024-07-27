import numpy as np
from scipy.spatial.distance import euclidean
from itertools import permutations
import random

# Define city coordinates
city_coords = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72)
}

# Calculate euclidean distances between each pair of cities
distances = {}
num_cities = len(city_coords)
for i in range(num_cities):
    for j in range(i + 1, num_cities):
        dist = euclidean(city_coords[i], city_coords[j])
        distances[frozenset([i, j])] = dist

# Function to calculate the total travel distance of a route
def calculate_total_distance(route):
    total_dist = 0
    for i in range(len(route) - 1):
        total_dist += distances[frozenset([route[i], route[i + 1]])]
    return total_dist

# Genetic Algorithm parameters
num_generations = 1000
population_size = 100
mutation_rate = 0.1
tour_length = 13

# Initialize random population
population = []
for _ in range(population_size):
    random_tour = random.sample(city_coords.keys(), tour_length)
    if 0 not in random_tour:
        random_tour[-1] = 0  # Ensure depot is in the tour
    population.append(random_tour + [random_tour[0]])

# Fitness function to minimize the total travel distance
def fitness_function(tour):
    return calculate_total_distance(tour)

# Genetic Algorithm functions
def crossover(parent1, parent2):
    start = random.randint(0, tour_length - 2)
    end = random.randint(start, tour_length - 1)
    child = [None] * tour_length
    child[start:end] = parent1[start:end]
    filled = set(parent1[start:end])
    pos = 0
    for city in parent2:
        if city not in filled and None in child:
            while child[pos] is not None:
                pos += 1
            child[pos] = city
            filled.add(city)
    child.append(child[0])  # complete tour back to depot
    return child

def mutate(tour):
    if random.random() < mutation_rate:
        i, j = random.sample(range(tour_length), 2)
        tour[i], tour[j] = tour[j], tour[i]
    return tour

# Run genetic algorithm
best_tour = None
best_distance = float('inf')

for generation in range(num_generations):
    # Evaluate the current population
    ranked_tours = sorted(population, key=fitness_function)
    population = ranked_tours[:population_size // 2]  # select half best

    # Crossover and mutate to create next generation
    next_generation = []
    while len(next_generation) < population_size:
        parent1, parent2 = random.sample(population, 2)
        child = crossover(parent1, parent2)
        child = mutate(child)
        next_generation.append(child)

    population = next_generation
    current_best_tour = ranked_tours[0]
    current_best_distance = fitness_function(current_best_tour)

    if current_best_distance < best_distance:
        best_tour = current_best_tour
        best_distance = current_best_distance

# Display result
print("Tour:", best_tour)
print("Total travel cost:", best_distance)