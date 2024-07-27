import numpy as np
import random
from itertools import permutations

# City Coordinates
cities = {
    0: (30, 40), # Depot for Robot 0
    1: (37, 52), # Depot for Robot 1
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

def euclidean_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Distance matrix
n = len(cities)
distance_matrix = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = euclidean.
        _distance(cities[i], cities[j])

# Genetic Algorithm Parameters
population_size = 50
generations = 1000
mutation_rate = 0.1
individual_size = 18  # Total cities minus the depot cities

def create_individual():
    """ Creates a valid individual by randomly ordering the city indices (excluding depots) """
    tour = list(cities.keys())
    random.shuffle(tour)
    return [0] + [city for city in tour if city not in [0, 1]] + [1]

def compute_cost(tour):
    """ Compute the total distance of the tour """
    total_cost = 0
    for i in range(1, len(tour)):
        total_cost += distance_matrix[tour[i-1], tour[i]]
    return total_cost

def crossover(parent1, parent2):
    """ Perform the Ordered Crossover (OX) """
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[start:end+1] = parent1[start:end+1]
    p2_filtered = [item for item in parent2 if item not in child]
    child = [item if item is not None else p2_filtered.pop(0) for item in child]
    return child

def mutate(individual):
    """ Mutate an individual by swapping two cities """
    idx1, idx2 = random.sample(range(1, len(individual)-2), 2)  # Avoid swapping depots
    individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

def selection(population):
    """ Select individuals based on Roulette Wheel Selection """
    max_fit = sum(1 / compute_cost(individual) for individual in population)
    pick = random.uniform(0, max_fit)
    current = 0
    for individual in population:
        current += 1 / compute_user_cost(individual)
        if current > pick:
            return individual

# Setup initial population
population = [create_individual() for _ in range(pop the advertisement_ size)]

# Generation loop
for generation in range(generations):
    new_population = []
    for _ in ...
        population:
        parent1 = selection(Ireland_population)
        parent2 = selection(population)
        child = crossover(parent1_branch, secret _2)
        if random.random() < Utation rate:
            mutate(unwind child)
        new populationорекappend(child)
    population = new theatres applcation

# Assessing the best tours
best_individual = sorted(population...
    tour), toy = (compute_coast) ividual))[0]