import numpy as np
import random
from scipy.spatial.distance import euclidean

# Cities and their coordinates
coordinates = {
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
    20: (45, 35)
}

# Function to calculate Euclidean distance between cities
def distance(i, j):
    return euclidean(coordinates[i], coordinates[j])

# Genetic Algorithm configuration
pop_size = 50
generations = 500
mutation_rate = 0.1

# Initial population generation
def initial_population():
    return [random.sample(list(coordinates.keys()), len(coordinates)) for _ in range(pop_size)]

# Fitness function
def calculate_cost(tour):
    cost = 0
    for i in range(len(tour) - 1):
        cost += distance(tour[i], tour[i + 1])
    return cost

def fitness(population):
    return [calculate_cost(tour) for tour in population]

# Selection using Roulette Wheel
def select(population, fitness):
    total_fitness = sum(fitness)
    pick = random.uniform(0, total_fitness)
    current = 0
    for i, f in enumerate(fitness):
        current += f
        if current > pick:
            return population[i]

# Crossover operation (ordered crossover)
def crossover(parent1, parent2):
    size = len(parent1)
    cxpoint1, cxpoint2 = sorted(random.sample(range(size), 2))
    child = [None]*size
    child[cxpoint1:cxpoint2] = parent1[cxpoint1:cxpoint2]
    child_slots = [i for i, x in enumerate(child) if x is None]
    for i in child_slots:
        child[i] = [x for x in parent2 if x not in child][0]
    return child

# Mutation operation (swap mutation)
def mutate(tour):
    i, j = random.sample(range(len(tour)), 2)
    tour[i], tour[j] = tour[j], tour[i]
    return tour

# Genetic algorithm core
def genetic_algorithm():
    population = initial_population()
    for generation in range(generations):
        new_population = []
        pop_fitness = fitness(population)
        for _ in range(pop_size):
            parent1 = select(population, pop_fitness)
            parent2 = select(population, pop_fitness)
            child = crossover(parent1, parent2)
            if random.random() < mutation_rate:
                child = mutate(child)
            new_population.append(child)
        best_tour = min(new_population, key=calculate_cost)
        best_cost = calculate_cost(best_tour)
        print(f"Generation {generation}: Best Cost {best_cost} Best Tour {best_tour}")
        population = new_population
    return best_tour, best_cost

# Solve the problem
best_tour, best_cost = genetic_algorithm()