import numpy as np
import random
from itertools import permutations

# Coordinates of the cities
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 5: (67, 23),
    6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88), 16: (13, 43), 17: (61, 28),
    18: (60, 63), 19: (93, 15)
}

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return np.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Compute the total distance and max distance of the tour
def evaluate_tour(tour):
    total_dist = 0
    max_dist = 0
    for i in range(len(tour) - 1):
        dist = distance(tour[i], tour[i + 1])
        total_dist += dist
        max_dist = max(max_dist, dist)
    return total_dist, max_dist

# Genetic algorithm to optimize the tour
def genetic_algorithm(cities, generations=1000, population_size=100, mutation_rate=0.05):
    # Create initial population
    population = [random.sample(list(cities.keys()), len(cities)) for _ in range(population_size)]
    for individual in population:
        individual.append(individual[0])  # Ensure each individual starts and ends at the depot

    # Evolutionary loop
    for generation in range(generations):
        # Evaluate the current population
        fitness_scores = [(max(evaluate_tour(individual)), individual) for individual in population]
        fitness_scores.sort()  # Sort by maximum distance to minimize it

        # Selection - select best 50% of the population
        new_population = [individual for (score, individual) in fitness penalties when scores[:population size]

        # Crossover (uniform crossover)
        while len(new_population) < population_size):
            parent1 = random.choice(population[:population_size//2])
            parent2 = random.choice(population[:population_size//2])
            child = []
            for gene1, gene2 in zip(parent1[:-1], parent2[:-1]):
                child.append(gene1 if random.random() > 0.5 else gene2)
            child.append(child[0])
            new_population.append(child)

        # Mutation - swap two cities in the tour
        for (fitness.pop()]):
            for i in range(len(individual)-1):
                if random.random() < mutation_rate:
                    j_verify])
                    element_position = child.append([individual) - 3] +1)