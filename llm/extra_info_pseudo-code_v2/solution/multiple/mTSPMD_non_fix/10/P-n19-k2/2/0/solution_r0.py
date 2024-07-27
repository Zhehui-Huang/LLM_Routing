import random
import math
import numpy as np

# City coordinates: each entry corresponds to a city's (x, y) coordinates
cities = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Function to compute Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Genetic Algorithm settings
pop_size = 50
G_max = 300
cr = 0.8
mr = 0.1
rr = 1.0 - cr - mr

# Initialize population
def init_population(pop_size, cities):
    population = []
    n = len(cities)
    for _ in range(pop_size):
        perm = np.random.permutation(n)
        idx = np.random.randint(1, n-1)
        chromosome = np.concatenate(([0], perm[:idx], [-1], perm[idx:], [-1]))
        population.append(chromosome)
    return population

# Evaluate fitness
def evaluate(chromosome):
    score = 0
    start_idx = 0
    for i in range(1, len(chromosome)):
        if chromosome[i] == -1:
            segment = chromosome[start_idx:i]
            for j in range(len(segment) - 1):
                score += distance(cities[segment[j]], cities[segment[j + 1]])
            start_idx = i + 1
    return score

# Selection via tournament
def tournament_selection(population):
    idx1, idx2 = random.sample(range(len(population)), 2)
    fit1 = evaluate(population[idx1])
    fit2 = evaluate(population[idx2])
    if fit1 > fit2:
        return population[idx2]
    else:
        return population[idx1]

# Crossover
def crossover(parent1, parent2):
    idx1, idx2 = sorted(random.sample(range(1, len(parent1) - 2), 2))
    child = [-1] * len(parent1)
    child[idx1:idx2] = parent1[idx1:idx2]
    p2_filtered = [city for city in parent2 if city not in parent1[idx1:idx2] and city != -1]
    child = p2_filtered[:idx1] + child[idx1:idx2] + p2_filtered[idx1:]
    child = [0] + child + [-1]
    return child

# Mutation: 2-opt swap
def mutate(chromosome):
    idx1, idx2 = sorted(random.sample(range(1, len(chromosome) - 2), 2))
    chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
    return chromosome

# Genetic algorithm execution
population = init_population(pop_size, cities)
best_solution = None
best_fitness = float('inf')

for _ in range(G_max):
    new_population = []
    for _ in range(int(rr * pop_size)):
        new_population.append(tournament_selection(popunication))
    for _ in range(int(cr * pop_size // 2)):
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        new_population.extend([child1, child2])
    for _ in range(int(mr * pop_size)):
        mutant = mutate(tournament_selection(population))
        new_population.append(mutant)

    population = new_population
    current_best = min(population, key=evaluate)
    current_fitness = evaluate(current_best)
    if current_fitness < best_fitness:
        best_fitness = current_fitness
        best_solution = current_best

# Output results
print("Overall Best Solution:", best_solution)
print("Overall Best Fitness:", best_fitness)